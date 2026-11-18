import socket
import threading

HOST = "127.0.0.1"
PORT = 8080

choices = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

state_lock = threading.Lock()
send_lock = threading.Lock()
stop = threading.Event()
current_round = None


def send_line(client, text):
    try:
        with send_lock:
            client.sendall((text + "\n").encode("utf-8"))
        return True
    except OSError:
        return False


def choose_username(client, reader):
    while True:
        try:
            username = input("Enter username: ").strip()
        except (EOFError, KeyboardInterrupt):
            return None

        if username.lower() == "/exit":
            return None

        if not username or len(username) > 20 or "|" in username or username.startswith("/"):
            print("Invalid username!")
            continue

        if not send_line(client, username):
            print("Server disconnected.")
            return None

        response = reader.readline()

        if not response:
            print("Server disconnected.")
            return None

        response = response.strip()

        if response.startswith("WELCOME|"):
            print(f"Welcome, {username}!")
            return username

        if response == "TAKEN":
            print("Username already taken!")
        elif response == "EMPTY":
            print("Username cannot be empty!")
        elif response == "INVALID_USERNAME":
            print("Invalid username!")


def receive(reader):
    global current_round

    while True:
        try:
            line = reader.readline()
        except (OSError, ValueError):
            line = ""

        if not line:
            if not stop.is_set():
                print("\nServer disconnected. Press Enter to exit.")
            stop.set()
            return

        message, _, data = line.strip().partition("|")

        if message == "START":
            with state_lock:
                current_round = data

            print(f"\n===== ROUND {data} =====")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            print("Enter 1, 2, 3 or /exit to leave:")

        elif message == "CHOICE_OK":
            print("Choice submitted. Waiting for other players...")

        elif message == "RESULT":
            with state_lock:
                current_round = None

            print("\n===== ROUND RESULT =====")
            print(data)

        elif message == "CANCEL":
            with state_lock:
                current_round = None

            print("\nRound cancelled:", data)
            print("Waiting for players...")

        elif message == "INVALID":
            print("Invalid:", data)

        elif message in ("NOT_IN_ROUND", "ALREADY"):
            print(data)

        elif message == "BYE":
            print("Goodbye!")
            stop.set()
            return


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except OSError:
        print("Could not connect to the server.")
        client.close()
        return

    reader = client.makefile("r", encoding="utf-8")
    receiver = None

    try:
        if choose_username(client, reader) is None:
            return

        print("Waiting for players...")

        receiver = threading.Thread(target=receive, args=(reader,), daemon=True)
        receiver.start()

        while not stop.is_set():
            try:
                text = input().strip().lower()
            except (EOFError, KeyboardInterrupt):
                text = "/exit"

            if stop.is_set():
                break

            if text == "/exit":
                send_line(client, "/exit")
                receiver.join(timeout=3)
                break

            selected = choices.get(text)

            if selected is None and text in choices.values():
                selected = text

            if selected is None:
                print("Invalid choice! Enter 1, 2, 3 or /exit.")
                continue

            with state_lock:
                round_id = current_round

            if round_id is None:
                print("No active round. Please wait.")
                continue

            if not send_line(client, f"CHOICE|{round_id}|{selected}"):
                print("Server disconnected.")
                break

    except (OSError, ValueError):
        print("Connection error.")

    finally:
        stop.set()

        try:
            client.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass

        if receiver is not None:
            receiver.join(timeout=1)

        try:
            reader.close()
        except (OSError, ValueError):
            pass

        client.close()


if __name__ == "__main__":
    main()
