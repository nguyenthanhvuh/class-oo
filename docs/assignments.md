
# Schedule (Tentative)

## Week 1

- Topic: Class Overview
- Reading:  OOP 1 / OOP 2
- In-class:  Specification for Sorting in OOP 2, User Equality in OOP 2
- HW Assignment: [HW1](#hw1)

## Week 2

- Topic: Procedural Abstraction (Specifications)
- Reading: OOP 2 
- In-class: Tail (total) function
- HW Assignment: Loan Calculator

## Week 3

- Topic: Data Abstraction and Abstract Data Type (ADT)
- Reading: OOP 3
- In-class: Stack ADT
- HW Assignment: Polynomial ADT


# In-Class Exercises




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

- Do the Loan Calculator assignment in Chapter 2 from the [OOP book](./oop.pdf) (2.3.3)

### Grading Criteria

1. Adherence to instructions.
1. Minimal implementation.
1. Preconditions are correctly converted to exceptions.
1. Python code runs correctly


## HW3
- Do the Polynomial ADT assignment in Chapter 3 from the [OOP book](./oop.pdf) (3.4.1)