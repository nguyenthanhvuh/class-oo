# INDEX
- [INDEX](#index)
- [Question 1](#question-1)
  - [1. enQueue](#1-enqueue)
    - [1.1 Partial Contract](#11-partial-contract)
    - [1.2 Total Contract](#12-total-contract)
  - [2. Rep Invariant](#2-rep-invariant)
  - [3. toString](#3-tostring)
  - [4. deQueueAll](#4-dequeueall)
  - [5. immutable deQueue](#5-immutable-dequeue)
  - [6. Clone](#6-clone)
- [Question 2](#question-2)
  - [1. repInvariant](#1-repinvariant)
  - [2. Contracts](#2-contracts)
  - [3. choose Method](#3-choose-method)
- [Question 3](#question-3)
  - [1. toString](#1-tostring)
  - [2. pushAll](#2-pushall)
  - [3. pop](#3-pop)
  - [4. equals](#4-equals)
- [Question 4](#question-4)
  - [1. Informal](#1-informal)
  - [2. Loop Invariants](#2-loop-invariants)
  - [3. Sufficiently strong loop invariant](#3-sufficiently-strong-loop-invariant)
  - [4. Insufficient strong loop invariant](#4-insufficient-strong-loop-invariant)
- [Question 5](#question-5)
  - [1. Correct](#1-correct)
  - [2. Differences](#2-differences)
  - [3. JUnit theories](#3-junit-theories)
  - [4. Testing vs Proving](#4-testing-vs-proving)
  - [5. Liskov Substitution Principle](#5-liskov-substitution-principle)
- [Question 6](#question-6)
  - [1. Mikalea Goldrich, Ramachandra Rao Seethiraju, Vaibhav Vijay Oza](#1-mikalea-goldrich-ramachandra-rao-seethiraju-vaibhav-vijay-oza)
    - [1.1 Mikalea Goldrich - (c)](#11-mikalea-goldrich---c)
    - [1.2 Ramachandra Rao Seethiraju - (c)](#12-ramachandra-rao-seethiraju---c)
    - [1.3 Vaibhav Vijay Oza - (b)](#13-vaibhav-vijay-oza---b)
- [Question 7](#question-7)



# Question 1

## 1. enQueue   
### 1.1 Partial Contract
``` java
    // PRECONDITION: e != null
    // POSTCONDITION: adds element to queue
    public void enQueue (E e) {
        elements.add(e);
        size++;
    }
```

### 1.2 Total Contract
To make the contract total we can not have any precondition. To remove the precondition we added a null check and throw an IAE exception.
``` java
    // PRECONDITION: none
    // POSTCONDITION: if e == null throwa IAE
    //                else adds the element to the queue
    public void enQueue (E e) throws IllegalArgumentException {
        if (e == null) throw new IllegalArgumentException();
        elements.add(e);
        size++;
    }
``` 

## 2. Rep Invariant
- elements.length == size
- all items in elements != null 


## 3. toString
We are printing all the className, queue lenght and all the items in the queue.
``` java
// PRECONDITION: none
// POSTCONDITION: returns a string representation of the queue object
public String toString() {
    String returnString = String.format("Queue Length: %d;\n", size);
    for(E element : elements) {
        returnString += String.format("\t%s\n", element.toString());
    }
    return returnString;
}
```

## 4. deQueueAll
We are copying the arraylist so we are not exposing the array reference.
The new list gets returned as a type that can be supertype of E in the type hierarchy.
``` java
// PRECONDITION: none
// POSTCONDITION: if there are no elements in the queue returns an empty queue
//                otherwise return a copy of all the elements of the queue
public List<? super E> dequeueAll() {
    return newArrayList<E>(elements);
}
```

## 5. immutable deQueue
The mutable deQueue operation does two things
1. Return the deQueued element.
2. Remove the deQueued element from the queue
   
To make deQueue immutable we need to split it into two methods.
1. deQueue() --> returns the queue without the first element.
2. peek() --> returns the first element in the queue.

``` java
// PRECONDITION: none
// POSTCONDITION: returns the first element in the queue
//                throws illegalStateException if the queue is empty
public E peek() throws IllegalStateException {
 if (size == 0) throw IllegalStateException();
 return elements.get(0);
}

// PRECONDITION: none
// POSTCONDITION: returns the current queue without the first element
//                throws IllegalStateException if the Queue is empty
public Queue<E> deQueue() throws IllegalStateException {
    if (size == 0) throw IllegalStateException();
    Queue<E> newQueue = new Queue();
    for (int i=1; i < size; i++) {
        newQueue.enQueue(elements.get(i));
    }
    return newQueue
} 
```

## 6. Clone
We have to ensure that the queue class implements cloneable so we can override the clone method.
We also have to downcast the cloned object to our Queue class and supress any unchecked cast exceptions.
The cloned object is only a shallow clone and not a recursive clone of all the items in the array list, as this would make the implementation very messy and would require the type of E to implement clonable also.


``` java
// PRECONDITION: none
// POSTCONDITION: returns a clone of queue
//                if any of the superclasses in the type hierarchy do not implement clonable throw AssertionError  
    public Queue<E> clone() { 
        try {
            @SuppressWarnings("unchecked")
            Queue<E> queue = (Queue<E>) super.clone();            
            return queue;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }    
    }  
```

# Question 2
## 1. repInvariant
- each item in choiceList != null
- choiceList != null
## 2. Contracts

```java
// PRECONDITION: none
// POSTCONDITON: instantiate this with the list, if a null element exists throw IAE if the list is null throw IAE
public GenericChooser (Collection<T> choices) {
    if (choices == null) throw new IllegalArgumentException();
    for (T choice : choices) {
        if (choice == null) throw new IllegalArgumentException();        
    }    
    choiceList = new ArrayList<>(choices);
}

// PRECONDITION: none
// POSTCONDITON: returns a randomly selected list item
public T choose() { 
    Random rnd = ThreadLocalRandom.current();
    return choiceList.get(rnd.nextInt(choiceList.size()));
}  
```

## 3. choose Method
The choose method is correct given the rep invariant and the contract are satisfied before and after `choose()` is called.


# Question 3
## 1. toString
- The toString() method exposes the internal state of the array by iterating over the entire array including removed items.
- The class name is not present

``` java
    @Override public String toString() {
        String result = "Stack size = " + size;
        result += "; elements = [";
        for (int i = 0; i < size; i++) {
            if (i < elements.length-1)
                result = result + elements[i] + ", ";
            else
                result = result + elements[i];
        }
        return result + "]";        
    }
```

## 2. pushAll
Push all violates encapsulation because it uses on the overridable `push()` method.
A subclass needs to be aware that the the push method needs to call the `ensureCapacity` method to not break the implementation.

``` java
// PRECONDITION: collection does not contain `null` elements
// POSTCONDITION: adds the entire collection to the stack
public void pushAll (Object[] collection) {
    for (Object obj: collection) { 
        push(obj); 
    }
}
```

## 3. pop
Pop in the mutable version does two things
1. return the item in the top of the stack
2. remove the item from the stack
   
The immutable version therefore needs to provide two methods
1. peek --> returning the item from the top of the stack
2. pop --> returning a stack witout the top item

``` java
// PRECONDITION: none
// POSTCONDITION: returns the last item in the current stack
//                throws ISE if the stack is empty
public Object peek () {
    if (size == 0) throw new IllegalStateException("Stack.peek");
        return = elements[--size];        
}

// PRECONDITION: none
// POSTCONDITION: returns a copy of the stack minus the last item
//                throws ISE if the stack is empty
public Stack pop () {
    if (size == 0) throw new IllegalStateException("Stack.pop");
        Stack stack = new Stack();        
        for (int i = 0; i < size -1; i++) {
            stack.push(elements[i]);
        }
}
```

## 4. equals
The current implementation requires us to check the equality of every item in the list with every other item, because different stacks with the same items can have different array lengths.
A list based implementation would allow us to use the equality method the list types provide.

# Question 4
## 1. Informal
- Any input Y will be greater than or equal to 1.
- X is initialized as 0
- add 2 to X as long as X < Y
- X >= Y
  - Case 1: Y is uneven eg. 1 => X > Y => 2 > 1
  - Case 2: Y is even number eg. 2 => X = Y => 2 = 2
- Post condition is true for all valid inputs 


## 2. Loop Invariants
- X >= 0; holds for all values of Y before and after loop
- X-1 <= Y; hold for all values of Y beofre and after loop
- Y > 0; same as above
  
## 3. Sufficiently strong loop invariant

> Weakest Precondition
```
WP(X:=0; while[X-1<=Y] X<Y do X:= X+2, {X >= Y})

1.  X-1 <= Y 

2.  (X-1 <= Y && X < Y)  => WP(X = X+2, {X-1<=Y}) 
    (X-1 <= Y && X < Y) => X+1 <= Y    
    True

3.  X-1 <= Y && !(X < Y) => X >= Y
    X = Y => X >= Y
    True

    X-1 <= Y && True && True
    WP(X:=0; X-1 <= Y) = -1 <= Y
```

> Verification Condition
```
    P => WP(X:=0; while[X-1 <= Y] X < Y do X:=X+2, {X >= Y})
    P => Y >= 1 => -1 <= Y
    Y >= 1 => Y >= -1
    True
```


## 4. Insufficient strong loop invariant

> Weakest Precondition
```
WP(Y:=0; while[X>0] X<Y do X:= X+2, {X >= Y})

1.  Y > 0 

2.  (Y > 0 && X < Y)  => WP(X = X+2, {Y>0})     
    False

3.  Y > 0 && !(X<Y) => X >= Y    
    False

    X > 0 && False && False => Not weakest pre-condition        
```


# Question 5
## 1. Correct
A program is correct if the rep invariant and the contract are satisfied for all methods.
> Correct Example
```java
    // REP INVARIANT: state any positive integer
    class Adder {
        private int state = 0;
        
    // PRECONDITON: none
    // POSTCONDITON: none
    public void addThree() {
        state += 3;
    } 
   }
```
> Incorrect: because method decrements state variable and renders rep invariant invalid.
```java
    // REP INVARIANT: state any positive integer
    class Adder {
        private int state = 0;
        
    // PRECONDITON: none
    // POSTCONDITON: none
    public void addThree() {
        state -= 3;
    } 
   }
``` 
## 2. Differences
- A contract defines the API for a consuner of a method or program, and does not expose implementation details to the user.
- A rep invariant defines the internal state the program needs to maintain before and after methods are executed. The rep invariant can be used to confirm the correct execution of the program during runtime.
- A loop invariant is a prediacte that needs to hold immediately before a loop gets called and immediatlely after each iteration. This allows us the verify the correctness of loops in some/not all cases.

## 3. JUnit theories
JUnit theories allow us to parameterize JUnit tests for a range of inputs and simplify testing when we want to test a large number of input combinations during testing.


## 4. Testing vs Proving
Testing can not prove the absence of errors, testing can only detect the presence of errors for the tested method/parameter combination.
Proving ensures that the program is valid for all inputs under the assumption that the program terminates.
If we cannot prove the correctness of a program it does not mean that the program is incorrect.

## 5. Liskov Substitution Principle
The Liskov Substitution Principle requires that any subtype X that inherits from a supertype Y can be used to replace Y and the program has to function correctly.
For this to hold, any subclass overriding a method has to satisfy the following.
- Weaker preconditions
- Stronger postcondition

The below Subclass satisfies Liskov's substitution principle because it has a Weaker precondition and a Stronger postcondition than the superclass and can therfore used in it's place.

SuperClass
```java
// PRE: this is not empty 
// POST: add five to this
public void addFive() {
    ...
}
```

SubClass extends SuperClass
```java
// PRE: none
// POST: add five to this, throw ISE if this is negative
public void addFive() {
    ...
}
```

# Question 6
## 1. Mikalea Goldrich, Ramachandra Rao Seethiraju, Vaibhav Vijay Oza
### 1.1 Mikalea Goldrich - (c)
### 1.2 Ramachandra Rao Seethiraju - (c)
### 1.3 Vaibhav Vijay Oza - (b)

# Question 7