import socket

def classify_temperature(temp):
    if temp < 10.0:
        return "Very Cold"
    elif 10.0 <= temp <= 24.9:
        return "Normal"
    elif 25.0 <= temp <= 34.9:
        return "Warm"
    elif 35.0 <= temp <= 44.9:
        return "High Temperature"
    else:
        return "Critical"

def start_server():
    HOST = 'localhost'
    PORT = 7070

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((HOST, PORT))
    print(f"Server is running...")

    while True:
        try:
            data, client_address = server_socket.recvfrom(1024)
            message = data.decode('utf-8').strip()

            if message == "/exit":
                print(f"Client {client_address} sent /exit shutting down server...")
                server_socket.sendto("Server shutting down Goodbye!".encode('utf-8'), client_address)
                break

            try:
                temperature = float(message)
                classification = classify_temperature(temperature)
                response = f"Temperature: {temperature}°C -> Classification: {classification}"
            except ValueError:
                response = "Error: Invalid input. Please enter a valid numerical temperature."

            server_socket.sendto(response.encode('utf-8'), client_address)

        except Exception as e:
            print(f"An error occurred: {e}")

    server_socket.close()

if __name__ == "__main__":
    start_server()
