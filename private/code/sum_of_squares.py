import threading
import multiprocessing
import time

def do_something(n, s):
    """Simulate a long-running task."""
    time.sleep(1)  # Simulate a delay
    print(f"{s} Working on input: {n}")

# Regular function
def regular_version(numbers):
    print("Regular version:")
    for number in numbers:
        do_something(number, "reg")

# Function using threads
def threaded_version(numbers):
    print("\nThreaded version:")
    threads = []
    
    for number in numbers:
        thread = threading.Thread(target=do_something, args=(number, "thread"))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Wait for all threads to finish

# Function using processes
def process_version(numbers):
    print("\nProcess version:")
    processes = []

    for number in numbers:
        process = multiprocessing.Process(target=do_something, args=(number, "process"))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to finish

if __name__ == "__main__":
    numbers = list(range(1, 6))  # Example list of numbers

    # Regular version
    regular_version(numbers)

    # Threaded version
    threaded_version(numbers)

    # Process version
    process_version(numbers)