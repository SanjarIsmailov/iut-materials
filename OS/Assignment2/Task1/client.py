import socket

HOST = "localhost"
PORT = 5000


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connected to IUT Canteen server.")
    print("Type a day (Monday or Mon). Type 'exit' to quit.")

    while True:
        day = input("Enter day: ").strip()
        if day.lower() == "exit":
            break
        if not day:
            continue

        client.sendall(day.encode("utf-8")) # send day to server
        reply = client.recv(1024).decode("utf-8") # get menu from server
        print("Server:", reply)

    client.close()
    print("Disconnected.")


if __name__ == "__main__":
    main()
