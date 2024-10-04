


# functions as first-class citizen of a language

def greet(name):
    return f"hello {name}"

f = greet 
print(f("419"))   # 1. assigning function as variable


def apply(f, a, b):
    return f(a,b)

def  pow(a, b):
    return a**b

def plus(a, b):
    return a+b

# print(apply(pow, 10,2))  # 2. pass function in as input

print(apply(plus, 10, 2))


# LISP
# John McCarthy
# Lamda expression
# Alonzo Church :  Turing Machine = Lamda Calculus 

square = lambda x:  x*x


def f():
    return lambda y: y+y



print(type(f))

# higher-order function
# map, reduce, filter
l = [1,2,3,4,5]


print(list(map(lambda x: x**x ,l)))

# Hadoop Spark 

# MapReduce Framework from Google:  Google FileSystem