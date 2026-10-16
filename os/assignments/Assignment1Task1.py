import threading

A = list(range(1, 31))


def sum_first_half():
    total = 0
    for i in range(15):
        total += A[i]
    print("Sum of 1st half:", total)


def sum_second_half():
    total = 0
    for i in range(15, 30):
        total += A[i]
    print("Sum of 2nd half:", total)


t1 = threading.Thread(target=sum_first_half)
t2 = threading.Thread(target=sum_second_half)

t1.start()
t2.start()

t1.join()
t2.join()

print("Total sum:", sum(A))
