from threading import Thread, Lock
import time

lock1 = Lock(); lock2 = Lock()

def t1():
    print("T1: Attempting to acquire Lock 1...")
    with lock1:
        print("T1: Acquired Lock 1.")
        time.sleep(1)  # Simulate some work

        print("T1: Attempting to acquire Lock 2...")
        with lock2:
            print("T1: Acquired Lock 2.")

def t2():
    print("T2: Attempting to acquire Lock 2...")
    with lock2:
        print("T 2: Acquired Lock 2.")
        time.sleep(1)  # Simulate some work

        print("T 2: Attempting to acquire Lock 1...")
        with lock1:
            print("T 2: Acquired Lock 1.")

if __name__ == "__main__":
    t1 = Thread(target=t1)
    t2 = Thread(target=t2)
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("Done.")