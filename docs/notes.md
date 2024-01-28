# Notes

## Module 1
- Syllabus 
  - No cheating 
  
- Correctness:
  - specification or contract ...
  - code is correct if it satisfies the contract
  - if you give it no contract, well then anything would be correct
  - so we want strong and precise contract


### Method/Program specifications
  - Preconditions: assumptions, properties about the inputs
    - established by clients (e.g., inputs are strings, unsorted list, ...)
      
  - Postconditions:  properties/behaviors of the method/program (usually related inputs)
    - done/established by the developers/implementations (e.g., outputs are sorted list, ...)

  - When something goes wrong, **who to blame**?
    - If preconditions are incorrect: blame the clients
    - If preconditions are correct, and the postconditions are not correct: blame developers


- Pre/Post conditions
   - specs/contracts consist of pre and postconditions
     - preconds (or requires)
     - postconds (or effects)
   - Example: __sorting a list_
     - preconds:  input is a list of *comparable* items
     - postcond:
       - output is sorted
       - output is a __permutation_ of data input
       
   - Precondition
     - as weak or general as possible
   - Postcondition 
     - as strong or precise as possible
     
- In class exercise
  - Equality (`__equals__` in Java or `_eq_` in Python)
  
  



## Module 2

### Weaker Preconditions and Stronger Postconditions
  
  - Reconsider the =intdiv= example from previous class
    
  ```java
  int intdiv(int x, int y){
    /*
    Return the integer division result x/y.
    

    precondition 
    - 
    -
    
    postconditions
    - if x or y are not integers, raise Exception
    - z is a number
    - z is an integer
    - if y is 0, then raise an Exception 
    - z*y ==  x
    */

    if not typeof(x, Int): raise 
    if not typeof(y, Int): raise     
    if (y == 0){ // raise ...
       ...     
    }
    return z
  }
  ``` 



    preconds:
    - x and y are integers # (already given in type)
    // - y cannot be zero   # better if we can remove this

    postconds:
    - z is a number  # weak
    - z is an integer  # weak
    - z = x // y  # *strong*
    ,*/



If we have `S1 = P => Q` and `S2 = P' => Q'`, then 
- S1 is better than S2 :   if P is weaker than P'
- S1 is better than S2 :   if Q is stronger than Q'


### Partial vs Total Contracts/Specifications
  - *partial* specification:  has a precondition
  - *total* specification:  has NO precondition

  - to turn a partial spec into a total spec:
    - for every precondition, remove and turn it into a new behavior in postcondition (of the form if not precondition, then do something, e.g., raising an excpetion)
      - E.g., if we have a precondition   =list= cannot be =null=
      - Then we remove that precondition
      - And create the postcondition:  if list is null then raise NullPointerExeception
   - in the implementation, create conditions and raise exception



### Check vs Unchecked Exception

   - precondition (purely specification):  if violated can gives undefine behavior
   - exception (more implementation): turn undefine behavior into defined ones
   - *checked exception** 
     - things that you should explicitly catch or rethrow
     - Block: throw checked exceptions for __recoverable conditions_ and _unchecked exceptions_ for programming errors. When in doubt, throw unchecked exceptions.
     <!-- - Liskov: -->
     <!--   - You should use an unchecked exception only if you expect that users will usually write code that ensures the exception will not happen, because -->
     <!--    • There is a convenient and inexpensive way to avoid the exception. -->
     <!--    • The context of use is local. -->
     <!--   - Otherwise, use checked -->

<!-- Otherwise, you should use a checked exception. -->
<!--      Most prefer Bloch's ... -->


### Check vs vs Unchecked (Bloch item 70)
   - check exception:  recoverable
     - force the caller to handle the exception
     - IOException: file not found,  well probably can have a backup , default one
     
   - unchecked exception:
     - recovery not possible
     - NPE: if you pass me a null pointer, and I try to dereference it, well then I should get NPE.  Not much I can do to turn a null pointer into a non-null pointer.  
       

### Item76: Strive for Failure Atomicity
   - failed method invocation should leave the object in the state that it was prior to the invocation
   - ways to achieve this
     - design immutable objects (tuples, string vs arrays, set)
       - performance, easy to reason about that (will spend more time later)
     - check the inputs
     - order the computation : parts that fail come before modification
     - write recovery code:  allow objecet to roll back its state
     - perform the operations on temporary copy of the object


** Abstraction
   - focuses on what (not how)
     - signature: formal parameters, return types, etc
     - isPrime:  detemrine if arg is prime is important ,   how this is determine is irrelevant

** Specifications/Contracts
   - Informal (English, remove example): easier to write but vague

int foo(string s, char d): ... 
 // pre: 
 // post
 // modify: s
 ....
 //implementation
  ..
 return 

** Signatures/Header
   - requires/modifies/effects   in comments
   - requires/precond: partial vs total  (partial: only for certain input so have require/preconditions,  total: for all correct type inputs, so precondition is TRUE, i.e. no precondition/require clause)
   - modifies: input modification -> side-effect
   - effects/postcond:  under assumption that requires are satisfied  (x' or x_post)
   - Precondition: weakest is best,  nothing (i.e., True) is even better
   - weaker vs stronger

** Implementation
   - Adhere to specifications
   - weaker vs stronger  , e.g., if specification says return a number, then always return 3 is ok.  but if specification says return an odd number, then cannot return any number.
   - 


IC2a
3. total specs

# pre:  Nothing
# post:
  1. if input list is null/None, throw NullPointException
  2. if input list is empty, throw Exception (or return [])
     - don't say anything about IndexError as that requires an Index-based datastructure in the implementation
  3. return the original list in the same order without first element
  4. remove the first element and return the rest: WRONG, X, too implemntation specific
  
# side-effects
  - Nothing

4. 


hasNext() Method:
  -Preconditions: Nothing explicitly mentioned in the Iterator interface documentation. It is generally assumed that the iterator is positioned at a valid element or at the end of the collection.

 - Postconditions:
   - Returns true if there is at least one more element in the collection; otherwise, returns false.

next() Method:
 - Preconditions: There is at least one more element in the collection.
indicating the end of the collection.
 - Postconditions:
   Returns the next element in the collection.
   The iterator is moved to the next position.
 
 - Violation Example: 
   - Calling next multiple times without calling 
hasNext to check if there are more elements.
   - Calling next when hasNext returns false,
 
 
remove() Method:
 - Preconditions: next() has been called at least once after the last call to remove.
 - Violation Example: Calling remove without first calling next.
Postconditions:
  Removes the last element returned by next from the underlying collection.
- Violation Example: Calling remove multiple times consecutively without calling next in between.


## Module 3
