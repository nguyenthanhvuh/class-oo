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






class Stack:
    """
    Rep-inv: 
    - contents cannot be null/None
    - stack is first in last out (FILO)
    - Def 1: if contents = [1,2,3], then that means 1 goes in first, then 2, then 3.  The last element of contents is the "top".
    - Def 2: if contents = [1,2,3], then that means 3 goes in first, then 2, then 1.  The first element of contents is the top
    """
    
    def __init__(self, l=[]):
        """
        constructor
        PRE: none
        POST: successfully creates an instance of Stack
        """
        self.contents = l
        
    def repOK(self):
        if not isinstance(self.contents, list):
            return False
        if not list: 
            return False
        
        #FILO
        #because push() uses Python append, it already correctly preserve the FILO order (e.g., [1,2,3].append(4) WILL result in [1,2,3,4])
        
        return True
    
    def push(self, x): 
        """
        MODIFIES: self
        PRE: none
        POST: append x to the top of the stack
        
        - [] -> [1]  
        - Stack([1,2,3]).push(4) ->  [1,2,3,4]
        """
        
        self.contents.append(x) # good for Def 1
        
    def push_immutable(self, x):
        """
        MODIFIES: NONE
        """
        new_obj = copy(self)
        new_obj.contents.append(x)
        return new_obj
        
    def pop(self):
        """
        PRE: none
        POST: remove the top of the stack and return the top of the stack
        
        - [] -> [1]  
        - Stack([1,2,3]).push(4) ->  [1,2,3,4]
        """
        
        ret = self.top()        
        self.contents.pop()
        return ret
    
    def pop_immutable(self):
        new_obj = copy(self)
        ret = self.top
        new_obj.contents.pop()
        
        return new_obj
    
    def return_top(self):
        return self.top
    
    def top(self):

        if not self:
            raise Exception(...)
        return self.contents[-1]
        
    
    def __str__(self):
        return str(self.contents)

        
        
# To Change from a Mutable ADT to Immutable, do these 2 steps:

# 1. change rep to private  (e.g., using private keyword in Java/C, and uses underscore __contents for Python)
# 2. for every mutator methods (e.g., push, pop in Stack), change it so that it returns the new object








class Mammal:
    def speak():
        print("say something")
class Dog(Mammal):
    def speak():
        print("woof")
class Cat(Mammal):
    def speak():
        print("meoow")

Dog d = Dog()
d.speak()    # static dispatching  ,  print "woof"

Mammal m = Dog() 
m.speak()    # dynamic dispatching , print "woof"  ??

animals = [d,  Cat()]
for a in animals:
    a.speak()
    
    



method_m(m: Mammal) 
    m.speak()
    
    
method_m(d)
    d.speak() 
    
    
method_d(c)
    c.speak()
    
    
    




LSP

Mammal.speak
- precond 
- postcond


Dog.speak
- precond
- postcond 


LSP:  
    - precond of method of a sublass needs be equal or weaker than the precond of a method of a superclass
        - precond of Dog.speak  weaker than or equal Mammal.speak
        

class A:
    def m(x):
        """
        pre: x <= 10 
        
        post: r >= 10
        """    
        
        return r
        
class B(A):
    def m(x):
        """
        pre: x <= 10
        pre: no constraint on X 
        pre: x <= 10 ,  x = 11 , x = 12,  ... , x=15    x <= 15
        pre: x <= 15 
        pre: x <= 100 
        
        post: r >= 20
        """
        return r
    
def method_m(a: A, x):
    a.m(x)

method_m(b) 



    