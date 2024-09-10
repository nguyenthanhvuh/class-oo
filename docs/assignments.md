
# Schedule (Tentative)

## Week 1

- Topic: Class Overview
- Reading:  Liskov 1--2
- In-class:  [IC1-A](#ic1-a), [IC1-B](#ic1-b) 
- HW Assignment: [HW1](#hw1)

## Week 2

- Topic: Procedural Abstraction (Specifications)
- Reading: Liskov 3
- In-class: [IC2-A](#ic2-a)
- HW Assignment: [HW2](#hw2)

## Week 3

- Topic: Procedural Abstraction
- Reading: Liskov 3
- In-class: [IC3-A](#ic3-a)
- HW Assignment: [HW3](#hw3)


# In-Class Exercises

## IC1-A

- Form a group of 3--4 students. 
- Work with your group and do the following:
    - Spend a few minutes getting acquainted. Explain a bit about yourself: full-time student?, working in software development?, why are you taking this class?, most/least favorite thing about writing software?, etc.
    - Decide on a mechanism for joint communication. Google docs? IDE with screen share? Something else?
- Consider a generic sorting method
    ```python
    def sort(my_list):
        # pre: 
        # post: 
        ...
    ```
    
    - Write the specification for the `sort` method (pre- and post-conditions).
    - Come up with several versions of pre and post-conditions. Discuss the pros and cons of each.


## IC1-B

This exercise touches on some thorny issues in data abstraction and inheritance. There is a lot going on in this example. Hence don’t worry if it seems confusing today. We’ll revisit this topic several times this semester.

Consider the following (textbook) code:

```python

# Do User first before doing SuperUser (much harder)

class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name

class SpecialUser(User):
    """Don't do this until you've done with User"""

    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def __eq__(self, other):
        if not isinstance(other, SpecialUser):
            return False
        return super().__eq__(other) and self.id == other.id
```

1. Look at the [Javadoc](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-) to understand the behaviors `equals()` (while this is in Java, the concept is the same in Python).
    - Specifically, read carefully the symmetric, reflexive, and transitive properties of `equals()` 
    - You can ignore the `consistency` property, which requires that if two objects are equal, they remain equal.
1. Is the given implementation of `equals()` in class `User` satisfy the 3 equivalence relation properties? If not, what is the problem?  Be concrete: find a specific object (test case!) that demonstrates the problem.
1. Is the given implementation of `equals()` in class `SpecialUser` satisfy the 3 equivalence relation properties? If not, what is the problem? Be concrete: find a specific object (test case!) that demonstrates the problem. How does *inheritance* makes `equals()` in class `SpecialUser` harder to get right?



## IC2-A

Consider the following code:

```python
def tail(my_list):
    # pre:  
    # post: 

    if not isinstance(my_list, list): 
        raise TypeError
    
    if not my_list:
        returns Exception


    result = my_list.copy()
    result.pop(0)
    return result
```
- Hint: also look at the Javadoc (for remove) or Python (for pop)

1. What does the implementation of `tail` do in each of the following cases? You might want to see the [Python document](https://docs.python.org/3/tutorial/datastructures.html) for `pop`.  How do you know: Running the code or reading Python document?
    1. `list = null` 
    1. `list = []`   
    1. `list = [1]`  
    1. `list = [1, 2, 3]`  #   return [2, 3]
1. Write a partial specification that matches the **happy path** part of the implementation’s behavior.
1. Rewrite the specification to be **total**. Use standard **exceptions** as needed.




# HW Assignments

## HW1

### Goal

1. getting started on Piazza
1. getting your group together

### Instructions

1. Sign up for Piazza (if you haven't already) and join our class page. The link and access code are in the syllabus.
1. Post a brief intro about yourself on the course Piazza page. For any credit, the posting must:
    - be a *follow-up* to my [introduction post](https://piazza.com/class/m0cjblb8hvd1qb/post/6). In other words, all intros need to be in the same thread.
    - Include a proper photo of yourself. (No sideways pictures, no oversize pictures, etc.)
1. Post your group on Piazza as a *follow-up* to my group [post](https://piazza.com/class/m0cjblb8hvd1qb/post/8).

### Grading Criteria

1. Your individual Piazza post adheres to my instructions. (That is, no sideways pictures, no oversize pictures, etc.) 
1. You are in a group.

## HW2

## Goals: Using Specifications

You'll build a small piece of Python from a given (partial) specification. Next, you will change the specification to **total** and modify your code accordingly.

### Instructions

Consider a function that calculates the number of months needed to pay off a loan of a given size at a fixed *annual* interest rate and a fixed *monthly* payment. For example, a $100,000 loan at an 8% annual rate would take 166 months to discharge at a monthly payment of $1,000, and 141 months to discharge at a monthly payment of $1,100. (In both cases, the final payment is smaller than the others; we round 165.34 up to 166 and 140.20 up to 141.) Continuing the example, the loan would never be paid off at a monthly payment of $100, since the principal would grow rather than shrink.

1. Implementation satisfying given specification: Define a Python class called `Loan`. In that class, write a function that satisfies the following specification:

    ```python
    class Loan:
        @staticmethod
        def months(principal: int, rate: float, payment: int) -> int:
            """
            Calculate the number of months required to pay off a loan.
            
            :param principal: Amount of the initial principal (in dollars)
            :param rate: Annual interest rate (e.g., 0.08 for 8%)
            :param payment: Amount of the monthly payment (in dollars)
            
            ::Requires (preconds): principal, rate, and payment all positive and payment is sufficiently large to drive the principal to zero.
            ::Effects (postconds): return the number of months required to pay off the principal
            """
    ```
    - Note that the precondition is quite strong, which makes implementing the method easy. The key step in your calculation is to change the principal on each iteration with the following formula (which amounts to monthly compounding):
        ```python
            new_principal = old_principal * (1 + monthly_interest_rate) - payment
        ```
    - To make sure you understand the point about preconditions, your code is required to be **minimal**. Specifically, if it is possible to delete parts of your implementation and still have it satisfy the requirements, you'll earn less than full credit.

1. *Total specification*: Now change the specification to **total** in which the postcondition handles violations of the preconditions using *exceptions*. In addition, provide a new implementation `month` that satisfies the new specification.

### Grading Criteria
    - Adherence to instructions.
    - Minimal implementation.
    - Preconditions are correctly converted to exceptions.
    - Python code runs correctly


## HW3
TBD