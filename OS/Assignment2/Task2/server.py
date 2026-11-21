#server
import socket

HOST = "localhost"
PORT = 8080

QUESTIONS = [
    ("Q1) What is a thread? A) A heavy process B) A lightweight unit of execution C) A type of memory", "B"),
    ("Q2) What is a kernel? A) A text editor B) A type of file C) The core part of the operating system", "C"),
    ("Q3) Which one is a scheduling algorithm? A) Round Robin B) Binary Search C) Quick Sort", "A"),
    ("Q4) What does RAM stand for? A) Read Access Memory B) Random Access Memory C) Run Active Memory", "B"),
    ("Q5) What is a deadlock? A) Processes wait for each other forever B) A fast CPU C) A full hard disk", "A"),
]


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Server is listening on", HOST, PORT)

    conn, addr = server.accept()
    print("Client connected:", addr)

    reader = conn.makefile("r")
    score = 0

    for question, correct in QUESTIONS:
        conn.sendall((question + "\n").encode())

        answer = reader.readline().strip().upper()
        if answer == "":
            print("Client disconnected.")
            break
        print("Client answered:", answer)

        if answer == correct:
            score += 1
            conn.sendall(b"Correct!\n")
        else:
            conn.sendall(b"Wrong!\n")
    else:
        conn.sendall(("Your score: " + str(score) + "/" + str(len(QUESTIONS)) + "\n").encode())

    conn.close()
    server.close()
    print("Server closed.")


main()
