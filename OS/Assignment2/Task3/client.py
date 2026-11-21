import socket

def start_client():
    SERVER_HOST = 'localhost'
    SERVER_PORT = 7070
    server_address = (SERVER_HOST, SERVER_PORT)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("Connected to Temperature Monitoring System.")
    print("Enter a temperature in Celsius or type '/exit' to quit.\n")

    while True:
        user_input = input("Enter temperature: ").strip()

        if not user_input:
            print("Input cannot be empty, Please try again!")
            continue

        client_socket.sendto(user_input.encode('utf-8'), server_address)

        data, _ = client_socket.recvfrom(1024)
        response = data.decode('utf-8')
        print(f"{response}\n")

        if user_input == "/exit":
            break

    client_socket.close()

if __name__ == "__main__":
    start_client()
