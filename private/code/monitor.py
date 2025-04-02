from threading import Thread, Condition
import time
import random

queue = []
lock = Condition()    
class ProducerThread(Thread):
    def run(self):
        global queue
        while True:
            num = random.choice(range(10)) 
            lock.acquire()
            queue.append(num)
            print("Produced", num)
            lock.notify()
            lock.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print("Nothing in queue"
                      "consumer waiting (instead of failing)")
                lock.wait()
                print("Producer added something to queue, consumer continues")
            num = queue.pop(0)
            print("Consumed", num)
            lock.release()
            time.sleep(random.random())

if __name__ == "__main__":
    ProducerThread().start()
    ConsumerThread().start()
