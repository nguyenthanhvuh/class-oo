


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



