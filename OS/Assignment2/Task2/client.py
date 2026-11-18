# client.py
import socket

HOST = "localhost"
PORT = 8080


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    reader = client.makefile("r")

    while True:
        message = reader.readline().strip()
        if message == "":
            break

        print("Server:", message)

        if message.startswith("Q"):

            answer = input("Client: ").strip().upper()
            client.sendall((answer + "\n").encode())
        elif message.startswith("Your score"):
            break

    client.close()
