# 8/26

## Example for Specification

Sorting (e.g., quicksort)
- Input: a list of integers numbers, e.g., [2,1,5,10]

- Output:  
  - *output is a permutation of input* and *output is in sored sorder (e.g., ascending)*
  
- Alg:
  - additional requirements, e.g., (involving pivot, worst case complexity n^2, amortized nlg n)
   
## Definitions 
Software Specifications (e.g., specification of a program/methoad/function)
 - *Preconditions*: properties of the Inputs
 - *Postconditions*: properties of the Outputs
   - Typically will have some relationships with the inputs
   
- Additional properties/specifications that are common for all software (desirable, but very hard to achieve)
  - secured
  - robust
  - bugs-free
  - efficiently
  
- Specification of a program: precondition + postcondition
- Correctness: A program (implementation) is *correct* if it satifies the given specifications (i.e., pre/post conditions).

## Another example

```
int intdiv(int x, int y):
  /*
  precond: x and y are integers, y cannot be zero
  postcond: z = x // y
  */
  

  return z
```


## In class Exercise (User, equals)
### Truth table for Implication (=>)

| X | Y | X => Y |
|---|---|--------|
| T | T | T      |
| T | F | F      |
| F | T | T      |
| F | F | T      |


Be careful about implication, the formula `X => Y` is only False when `X` is True but `Y` is False, in every other cases, the formula is True.


### Expected proeprties for an implementation of `equals` (according to [Javadoc](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html#equals(java.lang.Object)))
1. reflexive: `a == a`
1. symmetry:   `a == b <=>  b == a`
1. transitive: `a == b && b == c  =>  a == c`
 

- Examples
```
User u1("hello");
User u2("world")
User u3("swe419");

User u1a("hello");
User u1b("hello");
User u2a("world");

SpecialUser s1("hello", 1)
```

For the equal implementation in In-class 1B for User.

- Reflexive: OK
  - e.g., `u1.equals(u1): expected: T   impl: T`

- symmetry: OK
  - e.g., `u1.equals(u2): False  && u2.equals(u1): False    expected: F   impl: F`
  - `u1.equals(u1a): T  && u1a.equals(u1): T  expected: T  impl: T`

- Transitive: OK
  - e.g., `u1.equals(u2) &&  u2.equals(u3) =>  u1.equals(u3) expected: T impl: T`
          `u1.equals(u2a) &&  u2a.equals(u2b)  javadoc: T   impl: T`
          
          
Things become more complicated when involving inheritence

- Symmetry: Not OK
` u1.equals(s1)    impl:  T`
` s1.equals(u1)    impl:  F`

- A potential fix (suggested by a student)
```SpecialUser
      @Override public boolean equals (Object obj) {
      if (!(obj instanceof SpecialUser)) return super.equal(obj); //obj.equals(this)
       return super.equals(obj) && ((SpecialUser) obj).id == this.id;
      }
```      


