from multiprocessing import Process, Queue
import time

def square(numbers, queue):
    ct = 0
    for n in numbers:
        time.sleep(1)
        print(f"Square of {n}: {n*n}")
        ct += 1
    queue.put(ct)

def cube(numbers, queue):
    ct = 0
    for n in numbers:
        time.sleep(1)
        print(f"Cube of {n}: {n*n*n}")
        ct += 1
    queue.put(ct)

if __name__ == "__main__":
    numbers = [2, 3, 4, 5]

    queue = Queue()
    # Create processes
    process1 = Process(
        target=square,args=(numbers,queue))
    process2 = Process(
        target=cube,args=(numbers,queue))

    # Run processes (in parallel)
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    # Combine the counts from both processes
    total_ct = 0
    while not queue.empty():
        total_ct += queue.get()

    print("Count : ", total_ct)
    