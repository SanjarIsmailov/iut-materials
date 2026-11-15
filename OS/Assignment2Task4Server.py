import socket
import threading


clients = {}
lock = threading.Lock()


def broadcast(message):
    with lock:
        for client in list(clients.keys()):
            try:
                client.sendall(message.encode("utf-8"))
            except:
                pass


def handle_client(client, address):
    try:
        username = client.recv(1024).decode("utf-8").strip()

        if not username:
            client.close()
            return

        with lock:
            clients[client] = username

        print(f"{username} joined from {address}")

        broadcast(f"[Server]: {username} joined the group.\n")

        while True:
            data = client.recv(1024)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if message == "/exit":
                break

            broadcast(f"[{username}]: {message}\n")

    except ConnectionError:
        pass

    finally:
        with lock:
            username = clients.pop(client, None)

        client.close()

        if username:
            print(f"{username} left the group")
            broadcast(f"[Server]: {username} left the group.\n")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))

server.listen()

print(f"Server is running")

while True:
    client, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()
