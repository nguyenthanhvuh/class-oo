
# Schedule (Tentative)
## Week 1
- Topic: Class Overview
- Reading:  Liskov 1--2
- In-class:  [IC1-A](#ic1-a), [IC1-B](#ic1-b) 
- HW Assignment: [HW1](#hw1)

## Week 2
- Topic: Procedural Abstraction
- Reading: Liskov 3
- In-class: [IC2-A](#ic2-a)
- HW Assignment: [HW2](#hw2)

## Week 3
- Topic: Procedural Abstraction
- Reading: Liskov 3
- In-class: [IC3-A](#ic3-a)
- HW Assignment: [HW3](#hw3)


# In-Class Exercises

## IC1A
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

    


## IC1B
- Now address a technical topic. This exercise touches on some thorny issues in data abstraction and inheritance. There is a lot going on in this example. Hence don’t worry if it seems confusing today. We’ll revisit this topic several times this semester.

Consider the following (textbook) code:

```python
class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.name == other.name

class SpecialUser(User):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

    def __eq__(self, other):
        if not isinstance(other, SpecialUser):
            return False
        return super().__eq__(other) and self.id == other.id
```

1. Walk though the execution of the `equals()` method in class `User` for a few well-chosen objects as the parameter. What happens at each point in the execution?
1. What does it mean for an `equals()` implementation to be correct? How do you know? Be as concrete as you can.
    - Hint: look at the [Javadoc](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-) for `equals()`
1. Is the given implementation of `equals()` in class User correct? Again, be concrete. If there is a problem, find a specific object (test case!) that demonstrates the problem.
1. How does inheritance complicate the correctness discussion for `equals()` in class `SpecialUser?`
1. What is your assessment of the `equals()` method in the `SpecialUser` class?


## IC2-A

Consider the following code:

```python
def tail(my_list):
    # pre: my_list must not be None
    # post: returns a copy of my_list with the first element removed,
    #       or raises an IndexError if my_list is empty.

    result = my_list.copy()
    result.pop(0)
    return result
```
- Hint: also look at the Javadoc (for remove) or Python (for pop)

1. What does the implementation of `tail` do in each of the following cases? You might want to see the [Python document](https://docs.python.org/3/tutorial/datastructures.html) for `pop`.  How do you know: Running the code or reading Python document?
    1. `list = null`
    1. `list = []`
    1. `list = [1]`
    1. `list = [1, 2, 3]`
1. Write a partial specification that matches the **happy path** part of the implementation’s behavior.
1. Rewrite the specification to be **total**. Use standard **exceptions** as needed.
1. The resulting specification has a problem. What is it? (hint: specification should be more general and not tied to the implementation)
1. Rewrite the specification to address this problem. Rewrite the code to match the new specification.



# HW Assignments

## HW1

### Goal

1. getting started on Piazza
1. getting your group together.

### Instructions

1. Sign up for Piazza (if you haven't already) and join our class page. The link and access code are in the syllabus.
1. Post a brief intro about yourself on the course Piazza page. For any credit, the posting must:
    - be a *follow-up* to my introduction post. In other words, all intros need to be in the same thread.
    - Include a proper photo of yourself. (No sideways pictures, no oversize pictures, etc.)
1. Your group should communicate the composition of your group to me (and the GTA) on Piazza.

### Grading Criteria

1. Your individual Piazza post adheres to my instructions. (That is, no sideways pictures, no oversize pictures, etc.) 
1. You are in a group.

## HW2
TBD

## HW3
TBD