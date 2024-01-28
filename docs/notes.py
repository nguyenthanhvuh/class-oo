# specifications, contracts

def div(x:int, y:int):
    #precondition:  x: int, y:int, y != 0
    #postcondition: r:float, x==r*y + remainder

    if y == 0:
        raise Exception

    remainder = ...
    r:float = x/y

    return r

assert(div(10,2) == 5)
x = 10
y = 3
r = div(x,y)

print(x, r*y, x == r*y)


def ascending_sorting(input_list):
    #precond: input_list: list of finite integer numbers

    #postcond: |return_list| == |input_list|
    #return_list is sorted
    pass

def tail(my_list):
    # REQUIRES/PRECONDS: ???
    # EFFECTS/POSTCONDS: ???

    result = my_list.copy()
    result.pop(0)
    return result


def tail_test():
    # print(tail(None))
    # print(tail([]))
    print(tail([1]))
    print(tail([1,2,3]))

tail_test()
