import psutil,os,time

def fib_gen_naive(n: int) -> list[int]: 
    fib_sequence = [0,1]
    for _ in range(2,n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

class FibIterator:
    def __init__(self, max_count):
        self.a, self.b = 0, 1  # Initial values
        self.count = 0
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b  # Advance the sequence
        self.count += 1
        return value

def fib_iterator(n):
    return FibIterator(n)
    
def fib_generator(n: int):
    a, b = 0 ,1
    for _ in range(n):
        yield a
        a, b = b, a + b

def print_memory_usage(note=""):
    process = psutil.Process(os.getpid())
    print(f"- [memory] {note} consumes {process.memory_info().rss / (1024 * 1024):.2f} MB")
    
def test_me(f, n):
    print(f"invoking {f.__name__}({n})")
    st = time.time()
    result = f(n)
    ct = 0 
    for _ in range(n):
        ct += 1
    print(ct)
    print(f"- [Time] {f.__name__} takes {time.time() - st:.3f}s")
    print_memory_usage(f.__name__)

n = 10000000
#test_me(fib_generator, n)
test_me(fib_iterator, n)
#test_me(fib_gen_naive, n)

