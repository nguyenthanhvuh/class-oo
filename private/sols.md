# Document Title

Consider the program
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



**SOLUTION**: 

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

1. `i <= N` is a loop invariant at `[I]` because
    - it holds the first time we hit that location (`N>0` is the precond and `i =0` so we have `i<=N`)
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


2. (i <= N & !(i < N)) =>  i == N         # Grading: they do NOT need to do these simplifcations here. Can leave as is
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

#Grading: if they do not do simplification above then down here they will likey have to do it.  And the subsitution i -> 0 will help simplify many things. But whatever they did (simplify during the wp of while or down here), at this point should get 0 <= N
```

3. The `vc :  P => wp([i := 0, while [i<=N] (i<N) i := i + 1], i == N) ` is then
```
P => (0 <= N)
N >= 0 =>  0 <= N
True
```

4. Since the `vc` is shown to be valid (i.e., `True`), we have successfully prove that this program satisfies the given specs `P` and `Q`.
