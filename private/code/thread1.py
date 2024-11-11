from threading import Thread, Lock
import time

shared_ct = 0
lock = Lock()

def square(numbers):
    global shared_ct
    for n in numbers:
        time.sleep(1)
        print(f"Square of {n}: {n*n}")
        lock.acquire()
        # critical section
        shared_ct += 1  
        lock.release()        


def cube(numbers):
    global shared_ct
    for n in numbers:
        time.sleep(1)
        print(f"Cube of {n}: {n*n*n}")
        # locking the Python way
        with lock: 
            shared_ct += 1
        
if __name__ == "__main__":
    st = time.time()    
    numbers = [2, 3, 4, 5]
    
    # Create threads
    thread1 = Thread(target=square,
                     args=(numbers,))
    thread2 = Thread(target=cube, 
                     args=(numbers,))
    
    # Start the threads
    thread1.start(); thread2.start()

    # Wait for both threads to complete
    thread1.join(); thread2.join()

    print("Count : ", shared_ct)
    print(time.time() - st)
    