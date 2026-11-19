import socket

HOST = "localhost"
PORT = 5000

MENU = {
    "mon": ("Monday", "Plov"),
    "tue": ("Tuesday", "Lagman"),
    "wed": ("Wednesday", "Mastava"),
    "thu": ("Thursday", "Manti"),
    "fri": ("Friday", "Fish"),
}
WEEKEND = ("sat", "sun")


def get_response(text):
    day = text.strip().lower()[:3]  # "Monday" and "Mon" both become "mon"

    if day in MENU:
        full_name, dish = MENU[day]
        return f"{full_name}'s menu: {dish}"
    if day in WEEKEND:
        return "IUT Canteen is closed on weekends, try another day"
    return "Unknown day. Please send a day like Monday or Mon"


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"IUT Canteen server is listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    print("Student connected:", addr)

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            day = data.decode("utf-8")
            print("Received day:", day)
            conn.sendall(get_response(day).encode("utf-8"))

    server.close()
    print("Server stopped.")


if __name__ == "__main__":
    main()
