import threading
import time
import random
from multiprocessing import Process, Semaphore

class Election:
    def __init__(self):
        self.votes = {'Alice': 0, 'Bob': 0, 'Charlie': 0}
        self.lock = threading.Lock()

    def cast_vote(self, candidate):
        with self.lock:  
            if candidate in self.votes:
                self.votes[candidate] += 1
                print(f"Vote cast for {candidate}. Total votes: {self.votes[candidate]}")

    def tally_votes(self):
        with self.lock:  
            print(f"Current vote count: {self.votes}")

class Voter(threading.Thread):
    def __init__(self, election, semaphore):
        super().__init__()
        self.election = election
        self.semaphore = semaphore

    def run(self):
        candidates = ['Alice', 'Bob', 'Charlie']
        candidate = random.choice(candidates)
        self.semaphore.acquire()  # Acquire semaphore for voting
        self.election.cast_vote(candidate)
        time.sleep(random.uniform(0.1, 0.5))  # Simulate voting time
        self.semaphore.release()  # Release semaphore

class ElectionOfficial(Process):
    def __init__(self, election):
        super().__init__()
        self.election = election

    def run(self):
        time.sleep(1)  # Wait before tallying
        self.election.tally_votes()

if __name__ == "__main__":
    election = Election()
    semaphore = Semaphore(3)  # Allow up to 3 voters to vote simultaneously

    # Create voter threads
    voters = [Voter(election, semaphore) for _ in range(20)]
    
    # Create election official processes
    officials = [ElectionOfficial(election) for _ in range(2)]

    # Start all voters
    for voter in voters:
        voter.start()

    # Start all election officials
    for official in officials:
        official.start()

    # Wait for all voters to complete
    for voter in voters:
        voter.join()
        
    # Wait for all election officials to complete
    for official in officials:
        official.join()

    print("Election simulation completed.")