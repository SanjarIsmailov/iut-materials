import threading
import time
import random

def submit_assignment(student_id):
    print(f"Student {student_id} is submitting assignment at 23:59")
    time.sleep(random.uniform(0.5, 2))
    print(f"Student {student_id} is uploading assignment...")
    time.sleep(random.uniform(0.5, 2))
    print(f"Student {student_id} submitted assignment successfully!")

threads = []

for i in range(1, 8):
    t = threading.Thread(target=submit_assignment, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()
