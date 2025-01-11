

```
def div(a:Float, b:Float) -> Float:
    
    return the result of a/b
    
    
    Precondition (Requires): b has to be non-zero
    Postcondition (Effects): c = a/b  :   c*b  + r = a
    
    ...
    

    return c

```


```
def sort(inputs):

pre: 
- inputs should have comparable types

post:
- outputs is a permutation of input
- sorted (ascending)


outputs

... 

```



- 4 scenarios: 
  - pre is statisfied, post is satisfied :   OK 
  - pre is satisfied, post is not :    WRONG
  - pre is not satisfied, post is not satisfied:   OK 
  - pre is not satisfied, post is satisfied: OK 
  
  
  
  
# Precondition 

```python
def div(x:Float, y:Float) -> Float
    # comput z = x // y 
    
    # precon: None

    # postcond:
    # 1. z * y == x
    # 
    # 
    # ... 

    # if (y == 0):
    #     raise Exception("") ...
```

- a spec that has a precondition with 0 constraints (i.e., None) is called a **total** specification, o.w it is called *partial*
- to change from partial to *total* specs
    - for every precondition, just create code to handle it 
    - 

```python
def something(x: Int):
    # precondition
    1. x >= 10   # weaker
    2. x >= 100  # stronger

    # False  :  strongest possible precondition (i.e., the most useless one b/c it works with 0 inputs)
    1. 0 >= x >= 10
    2. -1 >= x >= 100

    # True : weakest possible precondition (i.e., total .. works with every input)

    # cannot compare pre-conditions
    # 1.   0 <= x <= 5   
    # 2.   -1 <= x <= 3  
```    


Postconditions