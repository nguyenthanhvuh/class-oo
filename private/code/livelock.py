import threading
import time

# Shared resource
resource = "Shared Resource"

# Two locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread_one():
    while True:
        with lock1:
            print("Thread 1: Acquired Lock 1")
            time.sleep(0.1)  # Simulate work

            if not lock2.acquire(timeout=0.1):
                print("Thread 1: Couldn't acquire Lock 2, releasing Lock 1")
                continue  # Release Lock 1 and try again

            print("Thread 1: Acquired Lock 2")
            break  # Successfully acquired both locks

def thread_two():
    while True:
        with lock2:
            print("Thread 2: Acquired Lock 2")
            time.sleep(0.1)  # Simulate work

            if not lock1.acquire(timeout=0.1):
                print("Thread 2: Couldn't acquire Lock 1, releasing Lock 2")
                continue  # Release Lock 2 and try again

            print("Thread 2: Acquired Lock 1")
            break  # Successfully acquired both locks

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_one)
    t2 = threading.Thread(target=thread_two)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done")
    