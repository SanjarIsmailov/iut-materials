import threading

balance = 0
lock = threading.Lock()

def deposit():
    global balance
    with lock:
        balance += 100
        print(f"Deposited: 100 | Balance: {balance}")
    with lock:
        balance += 200
        print(f"Deposited: 200 | Balance: {balance}")

def withdraw():
    global balance
    with lock:
        balance -= 50
        print(f"Withdrawn: 50 | Balance: {balance}")
    with lock:
        balance -= 100
        print(f"Withdrawn: 100 | Balance: {balance}")

t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=withdraw)

t1.start()
t1.join()
t2.start()
t2.join()
