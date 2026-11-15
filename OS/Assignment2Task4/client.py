import socket
import threading


def receive_messages(client):
    while True:
        try:
            data = client.recv(1024)

            if not data:
                print("\nDisconnected from server.")
                break

            print(data.decode("utf-8"), end="")

        except:
            break


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5000))

username = input("Enter your username: ")

client.sendall((username + "\n").encode("utf-8"))

receive_thread = threading.Thread(
    target=receive_messages,
    args=(client,),
    daemon=True
)

receive_thread.start()

while True:
    message = input()

    if message == "/exit":
        client.sendall("/exit\n".encode("utf-8"))
        break

    client.sendall((message + "\n").encode("utf-8"))

client.close()
