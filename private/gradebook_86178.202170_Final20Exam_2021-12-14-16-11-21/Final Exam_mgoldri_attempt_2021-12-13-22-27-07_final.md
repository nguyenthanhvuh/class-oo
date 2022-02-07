# Question 1

1. For `enQueue`, write (i) a partial contract and (ii) a total contract. For each part, if you need to change
   the code for the contract, do so and explain what you did
   1. **Partial** A partial contract is a contract with a precondition. In this example,
      e cannot be null.
```java
    /**
     * REQUIRES: e is not null
     * MODIFIES: this 
     * EFFECTS: Add e to the queue
     */
    public void enQueue (E e) {
        elements.add(e);
        size++;
    }
```
   2. **Total** A total contract does not include a precondition. In this example,
      we check if e is null in the code so that it is no longer a precondition
```java
    /**
    * MODIFIES: this
    * EFFECTS: Throw an IAE if e is null,
    *          else add e to the queue
    */
    public void enQueue (E e) throws IllegalArgumentException{
        if (e == null) {
        throw new IllegalArgumentException();
        }
        elements.add(e);
        size++;
    }
```

2. Write the rep invs for this class. Explain what they are.
   1. elements != null - The elements array cannot be null
   2. each element in elements != null - none of the elements in the array are null
   3. size == elements.length - Queue increments and decrements this.size as elements are added to the queue.

3. Write a reasonable `toString()` implementation. Explain what you did

      The `toString()` method should return a string representation  of the important attributes of the object.
      Here we include the size of the queue and each element in the queue.
```java
    public String toString() {
        String result = "size = " + size + "; elements = [";
        for (E e: elements) {
            result = result + e + " ";
        }
        return result + "]";
    }
```

4. Consider a new method, `deQueueAll()`, which does exactly what the name suggests. Write a reasonable
   contract for this method and then implement it. Be sure to follow Bloch’s advice with respect to
   generics. Explain what you did.

   For the `deQueueAll()` method, I iterate over the elements in the underlying array, remove each from the queue and
   add each to a new ArrayList which is then returned. 
   
   If there are no elements in the array, an `IllegalStateException` is thrown.

```java
    /**
     * MODIFIES: this
     * EFFECTS: Throw an IllegalStateException if there are no elements in the array,
     *          else remove (from the original queue) and return all the elements in the queue
     */
    public List<? extends E> deQueueAll() {
        if (size == 0) throw new IllegalStateException();
        ArrayList<E> allElements = new ArrayList<>();
        Iterator<E> iterator = elements.iterator();
        while (iterator.hasNext()) {
            allElements.add(deQueue());
        }
        return allElements;
    }
```

5. Rewrite the `deQueue()`
   
   For an immutable version of the Queue class, the deQueue method would return a new queue without the first element.
   
```java
    public Queue deQueueImmutable() {
       Queue<E> e = new Queue<E>();
       for (int i = 1; i < size; i++) {
           e.elements.add(elements.get(i));
       }
       return e;
    }
```

6. Clone method:
   First, call the super clone. Then create a new arraylist from the previous elements and assign it as the cloned 
   objects elements. This is to avoid sharing references between the two underlying data structures.
```java
      @Override public Queue clone() {
        try {
           Queue<E> result = (Queue) super.clone();
           result.elements = new ArrayList<E>(elements);
           return result;
        } catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
```

# Question 2
1. Rep invariants
   1. choiceList != null - the list of choices to pick from cannot be null
   2. choiceList.size() > 0 - there must be elements to pick from
2. Supply suitable contracts for the constructor and the `choose()` method and recode if necessary. The contracts should be consistent with your answer to the previous question. Explain exactly what you are doing and why.
   
   For the constructor, I check if the given choices collection is null or empty. If it is, I throw an
   IllegalArgumentError. This post-condition verifies that the rep invariants are met.
   
   For the `choose()` method, no code changes are required. Because of the rep invariants above,
   it is guaranteed that there will be at least one element in choices to choose from.
   
```java
    /**
     * EFFECTS: Throw an IAE if choices is null or empty
     * else add the given choices to the this
     */
    public GenericChooser (Collection<T> choices) {
        if (choices == null || choices.size() == 0) {
            throw new IllegalArgumentException();
        }
        choiceList = new ArrayList<>(choices);
    }

    /**
     * EFFECTS: Return a random choice from choices
     */
    public T choose() {
        Random rnd = ThreadLocalRandom.current();
        return choiceList.get(rnd.nextInt(choiceList.size()));
    }
```
3. Argue that the `choose()` method, as documented and possibly updated in your previous answers,
   is correct. You don’t have to be especially formal, but you do have to ask (and answer) the right
   questions. 
   
   The `choose()` method is correct because it satisfies both the rep invariants and the contract.

# Question 3
1. What is wrong with `toString()`? Fix it. 
   
   The `toString()` method exposes too much information by looping until elements.length not until size.

```java

    @Override public String toString() {
        String result = "size = " + size;
        result += "; elements = [";
        for (int i = 0; i < size; i++) {
            if (i < size-1)
                result = result + elements[i] + ", ";
            else
                result = result + elements[i];
        }
        return result + "]";
    }
```

2. As written, `pushAll()` requires documentation that violates encapsulation. Explain why and then write a contract for pushAll(). 
   The `pushAll()` method relies on the `push()` method. Suppose a developer creates a subclass of `StackInClass` that includes an isntance
   variable for `pushCount` which is incremented when an element is added to the stack. Because the subclass could use the `StackInClass`
   `pushAll()` method, pushes could be double counted.

```java
    /**
     *
     * EFFECTS: Throws an IAE exception if any of the elements in the collection are null.
     * else, adds each element in the collection to the stack.
     *
     * Implementation Requirements: This implementation uses the overridable `push` method.
     * For each element in collection, the push method is called which adds the element to the stack and 
     * increments size accordingly.
     */
    public void pushAll (Object[] collection) {
        for (Object obj : collection) {
            if (obj == null) {
                throw new IllegalArgumentException();
            }
        }
        for (Object obj: collection) {
            push(obj);
        }
    }
```

3. Rewrite the `pop()` method for an immutable version of the Stack class. Keep the same instance variables. Rewrite what you did. 
      
   The `pop()` method of an immutable StackInClass returns a new stack object without the 
   last element.

```java
    public StackInClass popImmutable () {
        if (size == 0) {
            throw new IllegalStateException("Stack.popImmutable");
        }
        StackInClass s = new StackInClass();
        for (int i = 0; i < size-1; i++) {
            s.ensureCapacity();
            s.elements[i] = elements[i];
        }
        return s;
    }
```

4. Implementing the equals() method for this class is a messy exercise, but would be much easier if the array was replaced by a list. Explain why. Note: You are not required to provide a implementation in your answer, but if you find it helpful to do so, that’s fine.

   By using a list instead of an array, we could rely on the `equals()` method of the list object. Whereas with the array,
   we have to manually loop over the elements up to `size` (not length) and compare each.

# Question 4

1. The precondition indicates that y >= 1 and x equals 0 at the start of the program. We will continue in 
   the loop as long as x < y and add two to x each time. Eventually, x with be greater than or equal to y, because
   for every one time we loop, we add 2. For example,
   1. y = 2 (meets precondition because 2 >= 1).
      - We go into the loop because 0 < 2.
      - x = 2 (0 + 2 = 2)
      - Then we do not go back into the loop because 2 < 2 == False
      - At the end of the program, the post-condition x >= y is met because 2 >= 2 == True
   2. y = 3 (meets precondition because 3 >= 1).
         - We go into the loop because 0 < 3.
         - x = 2 (0 + 2 = 2)
         - Then we go back into the loop because 2 < 3
         - Then we add 2 again; x = 4
         - Now we break out of the loop because 4 < 3 == False
         - At the end of the program, the post-condition x >= y is met because 4 >= 3 == True

2. A loop invariant must be true when the loop in entered and must be preserved after the loop body is executed.
   1. y >= 1
   
      According to the precondition, y is always greater than or equal to one and because we do not change y
      in the loop, it will still be greater than or equal to y after loop execution.
   2. x >= 0
   
      At the beginning of the loop, x equals zero (because it is assigned as zero right before the loop.
      In the body of the loop, we only increase x so it will never be less than 0. In other words, after the body of the loop,
      the loop invariant holds true because x >= 0.
   3. x <= y + 2
      
      At the beginning of the loop, x equals 0 and y is equal or greater than 1 so it holds true that x is less than or equal to y + 2.
      Each time through the loop, we increment x by 2. Eventually x could equal the original y but will never be greater than y + 2.
      For example, if y = 2. At the start of the loop, 0 <= 2+2 == True; Add 2 to x so 2 <= 2+2 == True; then we 
      do not reenter the loop so x is still less than or equal to y + 2 -> 2 <= 4 -- True.

3. Proof w/ loop invariant x ≤ y + 2
      
   ```
   WP(x:=0; while[x ≤ y + 2] x < y do x = x + 2, {x ≥ y}) =
   WP(x:=0; WP(while[x ≤ y + 2] x < y do x = x + 2, {{x ≥ y}) =
      1. x ≤ y + 2
      2. x ≤ y + 2 && x < y => WP(x = x + 2, {x ≤ y + 2})
         x < y => x + 2 < y + 2
         x < y => x < y
         True
      3. x ≤ y + 2  && ! x < y => x ≥ y
         x == y + 2 => x ≥ y
         True
         
   = x ≤ y + 2 && True && True
   = x ≤ y + 2
      
   WP(x:=0; {x ≤ y + 2})
   0 ≤ y + 2 
      
   VC
   P =>  WP(x:=0; while[x ≤ y + 2] x < y do x = x + 2, {x ≥ y})
   P => 0 ≤ y + 2 
   y ≥ 1 => 0 ≤ y + 2  # True
   ```
   The loop invariant x ≤ y + 2, proves the validity of the Hoare Triple because P implies the WP of the loop invariant as shown in the verification condition above.
4. Insufficiently strong loop invariant: x ≥ 0

   ```
   WP(x:=0; while[y ≥ 1] x < y do x = x + 2, {x ≥ y}) =
   WP(x:=0; WP(while[y ≥ 1] x < y do x = x + 2, {{x ≥ y}) =
      1. y ≥ 1
      2. y ≥ 1 && x < y => WP(x = x + 2, {y ≥ 1})
         x < y ≥ 0 => WP(x = x + 2, {y ≥ 1})

      3. y ≥ 1 0 && ! x < y => x ≥ y
         y ≥ 1 && x ≥ y => x ≥ y
         False
         
   = x ≤ y + 2 && False && False
   = False
   WP(x:=0; False) = False
   
   
   VC 
   P => Fakse
   y ≥ 1 => Fakse
   False
   ```
   
# Question 5
1. What does it mean that a program (or a method) is correct? Give (i) an example showing a program
(or method) is correct, an (ii) an example showing a program (or method) is incorrect.
   
   A program is correct if it stratifies the rep invariant of the class and the pre and post-conditions (aka contract)

   1. Question 2.3 shows a correct implementation of the `choose()` method 
   2. The below example is incorrect because the post-condition specifies that an IllegalArgumentException
   should be thrown if e == null however, the given code does not do so.
   ```java
   /**
   * EFFECTS: Throw an IAE if e is null, else add e to the stack.
   */
   public void push(E e){
        elements.add(e)
   }
   ```

2. Explain the difference between rep invariants, loop invariants, and contract/specifications (i.e., pre/post
   conds). Use concrete examples to demonstrate the difference.
   - A rep invariant shows what should always be true of a given class. For example, in question 2.1, those conditions
   should always be true when entering and exiting any method in the class.
   - Loop invariants indicate what should always be true when entering a loop and after the execution of the body of the loop.
   For example, in question 4.3, the loop invariant is true when we enter the loop and after the execution of the body.
   - Pre and post conditions indicate what should be true for the given inputs to a method and then what should happen 
   after method execution. These conditions should not include implementation details of the program. Pre and post conditions are 
   different from loop invariants. A pre condition must be true when entering a program and the post condition only needs to
   hold true after the program finishes. For example, in question 4. The post condition is explicitly not true at the beginning of the program,
   because x = 0 and y is at least 1. Therefore, the postcondition x >=y is false until the end of the program.
3. What are the benefits of using JUnit Theories comparing to standard JUnit tests. Use examples to
   demonstrate your understanding.
   
   Using JUnit theories allows us to easily test our programs on multiple inputs. Additionally, we can make assumptions about
   the preconditions and then assert our postconditions hold.
   Consider the following example below.
   - This test will run 9 times with each possible combination of the inputs
   - We can assume that each input is non-null which is a precondition for symmetry.
   - If both inputs are non-null, we assert that if a == b then b == a.

```java
@RunWith(Theories.class)
public class MyTest {
   @DataPoints
   public static String[] animals = {"cat", "cat", "dog"};

   @Theory
   public void symmetry(String sA, String sB) {
      assumeTrue(sA != null);
      assumeTrue(sB != null);

      Assert.assertTrue(sA.equals(sB) == sB.equals(sA));
   }
}
```

5. Explain the differences between proving and testing. In addition, if you cannot prove (e.g., using Hoare
   logic), then what does that mean about the program (e.g., is it wrong)?
   
   To prove a program is correct by using Hoare logic. There are two types of correctness: partial and total.
   **Partial** assume the precondition holds, if S successfully executes then the post condition holds. 
   We assume that the program terminates.
   **Total** we require that the program terminates. This is more difficult to prove.
   
   To test a program, we use testing tools like JUnit. We pass a variety of inputs to our programs and confirm we get hte expected output.
6. Explain the Liskov Substitution Principle (LSP). Use a concrete example to demonstrate LSP. Note:
   use a different example than the one given in Liskov
   
   The LSP says that the "subtype specification support reasoning based on the supertype specification." (Liskov 7.9).
   In other words, the precondition of the super type should be stronger than the precondition of the subtype
   and the precondition of the subtype should be stronger than the post-condition of the supertype.
   For example, consider the queue class from question 1. Recall that our `enQueue` method throws an IAE if the given 
   element to add to the queue is null. In the specification below, `MyQueue` is a subtype of `Queue`. However,
   our post-condition in `MyQueue` is less specific than that of the super type `Queue`. This violates LSP.
   
         ```java
         class MyQueue extends Queue {
              /**
              * EFFECTS: Adds the given element to the queue
              */
              public Object push(E e) {
           
              }  
         }
         ```
   
# Question 6
1. Ramachandra Rao Seethiraju: (c) Regular participant; contributed reliably
2. Mathias F Wiesbauer: (c) Regular participant; contributed reliably
3. Vaibhav Vijay Oza: (b) Occasionally attended, but didn’t contribute reliably

# Question 7
1. I liked that this class was online but it also made some of the material harder to understand. 
   I like the group work (though it is always challenging to schedule). I found it helpful to discuss the concepts with my group.
   Having the quiz at the end of class was very helpful; It gave us a chance to get refocused on the course and the material.
   I work full time so comign straight off of afternoon meetings to a quiz would have been challenging.
2. I like that you added a lecture on Hoare Logic.
3. I felt our team wasn't always prepared to start the in class exercises. I like when we would have
   some lecture/review prior to jumping in. 