import timeit
def gen_prime_non_iterator(n) -> list[int]:
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


n = 100000

# start = timeit.default_timer()
# gen_prime_non_iterator(n)
# print("etime ", timeit.default_timer() - start)  

class PrimeNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current >= self.n:
                raise StopIteration
            is_prime = True
            for j in range(2, self.current):
                if self.current % j == 0:
                    is_prime = False
                    break
            if is_prime:
                self.current += 1
                return self.current - 1
            self.current += 1


# start = timeit.default_timer()
# PrimeNumberIterator(n)
# print("etime ", timeit.default_timer() - start)  


def gen_prime_generator(n):
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i

        
print(type(gen_prime_generator))
start = timeit.default_timer()
gen_prime_generator(n)
print("etime ", timeit.default_timer() - start)  