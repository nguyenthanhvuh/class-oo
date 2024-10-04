


# closure 

def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier


print(make_multiplier(10)(100))
print(make_multiplier(3)(100))


    
def make_averager():
    deposits = []
    
    def myaverage(new_value):
        deposits.append(new_value)
        total = sum(deposits)
        return total / len(deposits)
    
    return myaverage

avg = make_averager()
print(avg(10))






def make_max_tracker():
    highest = 0
    
    def tracker(v):
        nonlocal highest
        highest = max(v, highest)
        return highest
    return tracker

max_tracker = make_max_tracker()

print(max_tracker(5))
print(max_tracker(3))
print(max_tracker(8))
print(max_tracker(7))

