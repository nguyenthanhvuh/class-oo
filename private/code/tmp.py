def foo(x: int, y: int):
    
    #l0 PC: True
    a = 0  ;  b = 0   
    # PS = {a->0 , b ->0}
    
    if x^3 == 1331:   #11 ^ 3
        # PC   x^3 == 1331
        a = 4
        # PS = {a -> 4,  b -> 0}
        if y % 6 == 0:
            # loc_error 
            # pc :  x^3 ==  1333 and y % 6 == 0
            
            # PS = {a -> 4, b -> 0}
            
            b = a + a
            # PS = {a -> 4, b -> 8}
        else:
            # l1 
            # pc: y % 6 != 0  and x ^3 == 1333
            a = 100
            # PS = {a -> 100, b -> 0}
            
            # pc: False
    else:
        # PS = {a -> 0, b -> 0}
        # pc x ^3 != 1333

    # 3 paths 
    # path 1:  PC: x^3 ==  1333 and y % 6 == 0 ,  PS  = {a->4, b->8}  
    # path 2:  PC: x ^3 != 1333,  PS = {a->0, b->0} 
    # path 3:  PC: y % 6 != 0  and x ^3 == 1333,  PS =  {a->100 ,b->0}
    
    assert(something ...)
    
    #l_end PC: ???     x^3 != 1331  OR   (x^3 == 1331 and y %6 == 0)
    #  when cannot reach l_end PC:   not (x^3 = 1331 and y % 6 != 0) =>  x^3 != 1331 or y %6 == 0 
    #   
    
            


# x^3 ==  1333 and y % 6 == 0
# (x = 11  ,  y == 12)  
# (x = 11 ,   y == -6 )


# symbolic execution
# - inputs as symbolic values 
# path condition (pc)   : condition over symbolic inputs to get to some loc of interest
# program state (ps):   values of variables
        
    
        
        
if (a1):
    #l1 
    ...
else:
    #l2 
    ...


if (a2):
    #l3
    ...
else:
    #l4 
    ...


if (a3):
    #l5
    ...
else:
    #l6
    ...

l1 l2 
l3 l4 
l5 l6

# 1.  l1 -> l3 -> l5 
# 2.  l2 -> l4 -> l6
# 3.  l1 -> l3 -> l6
# ... 
# 

a1 a2 a3     n  =3 
...
...
...

2^3   



a1 a2  .... an  
1  1        1
0  0        0
1  0  . . . 

2^n  -  c*n     O(2^n)


n = 1000 
2^n 
    
...
if (an):
    ...
else:
    ...

    
# n seque conditions:  ?? path    
    
i=0
while(i<1000):
    # do something
    i++ 
    bug occurs at iter i 
...    


1 iter :  if i < 100 :     do something   else:  ...
2 iter :  if i < 100 :     do something   else:  ...
3 iter :  if i < 100 :     do something   else:  ...

....
1000 iter:  ... 

# verification
# - formally guarantee will not fail under any possible inputs
# - pros:  can really provide guarantee (i.e.,  there's no possible way out of 2^100000000 that this program will crash).  
# - cons:  can be very expensive,  difficult to analyze


