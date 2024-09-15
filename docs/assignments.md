
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

- Topic: Data Abstraction and Abstract Data Type (ADT)
- Reading: Liskov 5
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

## IC3-A

Consider a simple generic `Queue` implementation.

```python
class Queue:
    """
    A generic Queue implementation using a list.
    """

    def __init__(self):
        """
        Constructor
        Initializes an empty queue.
        """
        self.elements = []
        self.size = 0

    def enqueue(self, e):
        """
        MODIFIES: self
        EFFECTS: Adds element e to the end of the queue.
        """
        self.elements.append(e)
        self.size += 1

    def dequeue(self):
        """
        MODIFIES: self
        EFFECTS: Removes and returns the element at the front of the queue.
        If the queue is empty, raises an IllegalStateException.
        """
        if self.size == 0:
            raise IllegalStateException("Queue.dequeue")
        
        result = self.elements.pop(0)  # Removes and returns the first element
        self.size -= 1
        return result

    def is_empty(self):
        """
        EFFECTS: Returns True if the queue is empty, False otherwise.
        """
        return self.size == 0


class IllegalStateException(Exception):
    """Exception raised when an invalid operation is attempted on an empty queue."""
    pass

```

1. Rewrite Queue to be *immutable*. Keep the representation variables `elements` and `size`.
1. Do the right thing with `enQueue()`.
1. Do the right thing with `deQueue()`.

## IC3-B

Consider the code 

```python
class Members:
    """
    Members is a mutable record of organization membership.
    AF: Collect the list as a set.
    rep-inv1: members != None
    rep-inv2: members != None and no duplicates in members.
    For simplicity, assume None can be a member.
    """

    def __init__(self):
        """Constructor: Initializes the membership list."""
        self.members = []  # The representation

    def join(self, person):
        """
        Post: person becomes a member.
        MODIFIES: self
        EFFECTS: Adds a person to the membership list.
        """
        self.members.append(person)

    def leave(self, person):
        """
        Post: person is no longer a member.
        MODIFIES: self
        EFFECTS: Removes a person from the membership list.
        """
        self.members.remove(person)
```

1. Analyze these four questions for *rep-inv 1*.
    1. Does `join()` maintain rep-inv?
    1. Does `join()` satisfy contract?
    1. Does `leave()` maintain rep-inv?
    1. Does `leave()` satisfy contract?
1. Repeat for *rep-inv 2*.
1. Recode `join()` to make the verification go through. Which rep-invariant do you use?
1. Recode `leave()` to make the verification go through. Which rep-invariant do you use?

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

- Do the Loan Calculator assignment in Section 2 from the [OOP book](./oop.pdf) (2.3.3)

### Grading Criteria

1. Adherence to instructions.
1. Minimal implementation.
1. Preconditions are correctly converted to exceptions.
1. Python code runs correctly


## HW3
- Do the Polynomial ADT assignment in Section 3 from the [OOP book](./oop.pdf) (3.4.1)