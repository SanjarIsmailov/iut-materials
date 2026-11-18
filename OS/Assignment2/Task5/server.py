import socket
import threading

HOST = "127.0.0.1"
PORT = 8080
MIN_PLAYERS = 2

players = {}
round_players = {}
condition = threading.Condition()
round_number = 0

beats = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def send(player, message):
    try:
        with player["lock"]:
            player["conn"].sendall((message + "\n").encode("utf-8"))
        return True
    except OSError:
        return False


def handle_client(conn, address):
    username = None
    key = None
    player = None
    reader = conn.makefile("r", encoding="utf-8")

    try:
        while True:
            raw = reader.readline()

            if not raw:
                return

            candidate = raw.strip()

            if not candidate:
                conn.sendall(b"EMPTY\n")
                continue

            if len(candidate) > 20 or "|" in candidate or candidate.startswith("/"):
                conn.sendall(b"INVALID_USERNAME\n")
                continue

            candidate_key = candidate.casefold()

            with condition:
                if candidate_key in players:
                    conn.sendall(b"TAKEN\n")
                    continue

                username = candidate
                key = candidate_key

                player = {
                    "name": username,
                    "conn": conn,
                    "lock": threading.Lock(),
                    "choice": None,
                    "score": 0
                }

                players[key] = player
                send(player, f"WELCOME|{username}")
                condition.notify_all()
                break

        while True:
            raw = reader.readline()

            if not raw:
                break

            message = raw.strip()

            if message.lower() == "/exit":
                send(player, "BYE")
                break

            parts = message.split("|", 2)

            if len(parts) != 3 or parts[0] != "CHOICE":
                send(player, "INVALID|Invalid command.")
                continue

            try:
                submitted_round = int(parts[1])
            except ValueError:
                send(player, "INVALID|Invalid round number.")
                continue

            choice = parts[2].strip().lower()

            if choice not in beats:
                send(player, "INVALID|Choose rock, paper, or scissors.")
                continue

            with condition:
                if round_players.get(key) is not player or submitted_round != round_number:
                    send(player, "NOT_IN_ROUND|This round is no longer active.")
                    continue

                if player["choice"] is not None:
                    send(player, "ALREADY|You already submitted a choice.")
                    continue

                player["choice"] = choice
                send(player, f"CHOICE_OK|{submitted_round}")
                condition.notify_all()

    except (OSError, ValueError):
        pass

    finally:
        with condition:
            if player is not None and players.get(key) is player:
                del players[key]

            condition.notify_all()

        try:
            reader.close()
        except (OSError, ValueError):
            pass

        try:
            conn.close()
        except OSError:
            pass

        print(f"{username or f'{address[0]}:{address[1]}'} disconnected")


def game_loop():
    global round_players, round_number

    while True:
        with condition:
            while len(players) < MIN_PLAYERS:
                condition.wait()

            round_number += 1
            round_players = players.copy()

            for player in round_players.values():
                player["choice"] = None
                send(player, f"START|{round_number}")

            while True:
                active = {
                    key: player
                    for key, player in round_players.items()
                    if players.get(key) is player
                }

                if len(active) < MIN_PLAYERS:
                    round_players = {}

                    for player in active.values():
                        send(player, "CANCEL|Not enough players.")

                    break

                if all(player["choice"] is not None for player in active.values()):
                    submitted = {player["choice"] for player in active.values()}
                    winners = []

                    if len(submitted) == 2:
                        winning_choice = next(
                            choice for choice in submitted
                            if beats[choice] in submitted
                        )

                        winners = [
                            player for player in active.values()
                            if player["choice"] == winning_choice
                        ]

                        for winner in winners:
                            winner["score"] += 1

                    choice_text = ", ".join(
                        f"{p['name']}: {p['choice']}"
                        for p in active.values()
                    )

                    score_text = ", ".join(
                        f"{p['name']}: {p['score']}"
                        for p in players.values()
                    )

                    if winners:
                        winner_names = ", ".join(p["name"] for p in winners)
                        result = (
                            f"Round {round_number}: {winner_names} won (+1). "
                            f"Choices: {choice_text}. Scores: {score_text}"
                        )
                    else:
                        result = (
                            f"Round {round_number}: DRAW. "
                            f"Choices: {choice_text}. Scores: {score_text}"
                        )

                    round_players = {}

                    for player in active.values():
                        send(player, f"RESULT|{result}")

                    break

                condition.wait()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on {HOST}:{PORT}")

    threading.Thread(target=game_loop, daemon=True).start()

    try:
        while True:
            conn, address = server.accept()
            threading.Thread(
                target=handle_client,
                args=(conn, address),
                daemon=True
            ).start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
