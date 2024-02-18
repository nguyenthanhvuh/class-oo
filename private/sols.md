# Consider the program
```
// {N >= 0}   # P
i = 0;
while (i < N){
    i = i + 1;
}

//{i == N}  # Q
```

1. Prove the program using the following the loop invariant: `i <= N`.
  1. Clearly reason why this is a loop invariant
  2. Compute the weakest precondition wp of the program wrt the post condition Q
  3. Compute the verification condition `vc : P => wp(..)`
  4. Analyze the `vc` to dertermine whether the program is proved or not
2. Repeat the above task a different loop invariant: `N >= 0`



## **SOLUTION**: 

For easier analysis, let's convert the program into this form: 
```
// {N >= 0}   # P
i = 0;
while (true)){
    [I]
    if (!(i < N)) break;
    i = i + 1;
}

//{i == N}  # Q
```

### Prove the program using the following the loop invariant: `i <= N`.

1. `i <= N` is a loop invariant at `[I]` because
    - it holds the first time we hit that location (`N>=0` is the precond and `i =0` so `i<=N` holds)
    - assume `i <= N` and the loop guard `i < N` holds, then `i <= N` is preserved through the loop body (the loop guard ensures that `i < N` and thus increment `i` by 1 will be `i + 1 < N` or `i <= N`)
     
     *Note for grading*: do not take off points if they do not list all the detail reasoning.  Give full points if they say something about `i < N` hits the first time enter the loop or hits that location, and that it is preserved the loop body.  


2. The WP of the program is 

```
wp([i := 0, while [i<=N] (i<N) i := i + 1], i == N)    # i <= N is the loop invariant, i == N is the Q
wp(i := 0, wp(while [i<=N] (i<N) i := i + 1, i == N))  # using wp for list of statements


let's do the wp of the while loop separately so it's clearer
wp(while [i<=N] (i < N) i := i + 1, i == N) = #   using wp for while, results in 3 conjuncts 

1. i <= N 

2. (i <= N & i < N) => wp(i := i + 1, i <= N)
   (i < N)          =>      i + 1 <= N      # Grading: they do NOT need to do these simplifcations here. Can leave as is
   (i < N)          =>      i  < N            
                   True                       


3. (i <= N & !(i < N)) =>  i == N         # Grading: they do NOT need to do these simplifcations here. Can leave as is
    (i <= N & i >= N)  =>  i == N
       i == N          =>  i == N         
               True
               
Thus wp(while [i<=N] (i < N) i := i + 1, i == N) = 

i <= N & True & True   
  i <= N                     #Grading: if they do NOT do the above simplification then this will be longer and the conjuncts of the 3 parts above
  
  
Now that we have th wp of while, let's finish the rest 
wp(i := 0, wp(while [i<=N] (i<N) i := i + 1, i == N)) 
= wp(i := 0, i <= N)   # put in the wp of while
= (i <= N)[i/0]               # using wp for assignment (i.e., subsitution i -> 0 in i <= N)
= 0 <= N

#Grading: if they do not do simplification above then down here they will likey have to do it.  And the subsitution i -> 0 will help simplify many things. 
```

3. The `vc :  P => wp([i := 0, while [i<=N] (i<N) i := i + 1], i == N) ` is then
```
P => (0 <= N)
N >= 0 =>  0 <= N
True
```

4. Since the `vc` is shown to be valid (i.e., `True`), we have successfully prove that this program satisfies the given specs `P` and `Q`.


### Prove the program using the following the loop invariant: `N >= 0`.
1. `N >= 0` is a loop invariant at `[I]` because
    - it holds the first time we hit that location (`N>=0` is the precond and `i =0` so `N>=0` holds)
    - assume `N >= 0` and the loop guard `i < N` holds, then `N >= 0` is preserved through the loop body (the loop body doesn't change `N`)
     
     *Note for grading*: do not take off points if they do not list all the detail reasoning.  Give full points if they say something about `N >=0` hits the first time enter the loop or hits that location, and that it is preserved the loop body.  


2. The WP of the program is 

```
wp([i := 0, while [N >= 0] (i<N) i := i + 1], i == N)    # N >= 0 is the loop invariant, i == N is the Q
wp(i := 0, wp(while [N >= 0] (i<N) i := i + 1, i == N))  # using wp for list of statements


let's do the wp of the while loop separately so it's clearer
wp(while [N >= 0] (i < N) i := i + 1, i == N) = #   using wp for while, results in 3 conjuncts 

1. N >= 0

2. (N >= 0 & i < N) => wp(i := i + 1, N >= 0)
   (N >= 0 & i < N) =>      N >= 0
              True                        # Grading: they do NOT need to do these simplifcations here. Can leave as is

3. (N >= 0 & !(i < N)) =>  i == N         
   (N >= 0 & i >= N)  =>  i == N         

               
Thus wp(while [N >= 0] (i < N) i := i + 1, i == N) = 

N >= 0 & True  &  (N >= 0 & i >= N)  =>  i == N
= N >= 0 &  (N >= 0 & i >= N)  =>  i == N
  
Now that we have th wp of while, let's finish the rest 
wp(i := 0, wp(while [N >= 0] (i<N) i := i + 1, i == N)) 
= wp(i := 0, N >= 0 &  (N >= 0 & i >= N))  =>  i == N)   # put in the wp of while
= (N >= 0 &  (N >= 0 & i >= N)  =>  i == N)[i/0]        # using wp for assignment (i.e., subsitution i -> 0 in i <= N)
= N >= 0 &  (N >= 0 & 0 >= N)  =>  0 == N
= N >= 0 &  (N >= 0 & 0 >= N)  =>  0 == N
= N >= 0 &       N == 0        =>  0 == N
= N >= 0 &          True
= N >= 0
```

3. The `vc :  P => wp([i := 0, while [N >= 0] (i<N) i := i + 1], i == N) ` is then
```
P => N >= 0
N >= 0 =>  N >= 0
True
```

4. Since the `vc` is shown to be valid (i.e., `True`), we have successfully prove that this program satisfies the given specs `P` and `Q`.



# Given the program
    ```
     // {x <= 1}   # P1
     // {x <= 11}  # P2

     while (x != 10){
         x := x + 1;
     }

     //{x == 10}  # Q
   ```
1. Informally reason that this program is correct with the given `P1` and `Q`.
The program starts with input `x` satisfying the precondition `x <= 1`, and thus will enter the loop and increment by 1 until `x = 10` and exit the loo. Thus the postcondition `x==10` holds.  

Note that if we use a different precondition, e.g., `x <= 11`, then the postcondition will not always hold because at the end of the program we might have `x==11`  

2. This program *is correct* with respect to the given precondition `P1` and postcondition `Q`.  Prove it by finding a loop invariant and verify the verification condition (show your work, i.e., generate the `wp` and the `vc` of the program, and reason about these)

We first change the program to 
    ```
     // {x <= 1}   # P1
     while (true){
         [I]
         if (!(x != 10)) break
         x := x + 1;
     }

     //{x == 10}  # Q
   ```

Let's use `x <= 10` as  loop invariant.  This is a loop invariant because 
-  `x <= 10` holds the first time it gets to `[I]`
-  Assume `x <= 10` and `x!= 10` (loop guard holds), `x <= 10` is preserved after the loop body   


We now compute the WP of the program wrt using `x <= 10` as loop invariant and `x == 10` as `Q` 
```
wp(while[x <= 10](x!=10) x := x + 1, x == 10)
= 
1. x <= 10

2. x <= 10 & x != 10 => wp(x := x+1, x <= 10)
  = (x <= 10 & x != 10) =>  x + 1 <= 10
  = (x <= 10 & x != 10)__ =>  x   <= 9
  =     x <= 9            =>  x   <= 9
  =               True

3. (x <= 10 & !(x != 10)) => x == 10
  = (x <= 10 & (x == 10)) => x == 10
  = x == 10 => x == 10
  = True

Thus the wp is x <= 10
```

The VC is then  
```
P1 => wp(..)
x <= 1 => x <= 10
True
```

Because the VC is valid, we have thus proved this program!

3. Now, consider a different precondition `P2`.
      1. Recompute the VC of the program with respect to `P2`.
      
      We can reuse our existing work on because the only thing changed was the precondition.  The VC is then
      ```
      P2 => wp(..)
      x <= 11 => x <= 10
      False
      ```
      
      
      2. is the VC  `P2 -> WP ..`  valid?  if yes, what does that mean,  if not, what does that mean?
      No, this VC is invalid.  This means that we cannot prove the program.   
      
      
