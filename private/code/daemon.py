from threading import Thread
import time

def daemon_task():
    while True: #long running
        print("Daemon thread running")
        time.sleep(1)

def regular_task():
    for i in range(10):
        print(f"Regular thread running: {i}")
        time.sleep(1)

if __name__ == "__main__":
    # a daemon thread
    daemon_t = Thread(target=daemon_task)
    daemon_t.daemon = True  # Set as daemon
    daemon_t.start()

    # a regular thread
    regular_t = Thread(target=regular_task)
    regular_t.start()
    regular_t.join()

    print("Done.")
    