# Quiz 1

## Specifications of Binary Search.

- Come up with the specifications for a binary search implementation whose header is given below. Remember for precondition you want something as weak as possible and for postcondition as strong as possible. Note that binary search returns the `location` (an integer) of the `target` value if found. It returns -1 if the `target` is not found. 

```python
def binary_search(arr: List[int], target: int) -> int:
    """
    PRE/REQUIRES: 
    POST/EFFECTS: 
    """
    ... 
```


<!-- # Quiz 2

Consider the following 2 specifications, the second of which has an
associated implementation:

``` java
public static int minIndex (int [] a) {... implementation omitted ... }
   // EFFECTS: if a null throw NullPointerException, else if a.length=0 throw
   //      IllegalArgumentException else return index of some min element in a.

public static void setSmall (int [] a, int i) {
   // REQUIRES: a != null, 0 <= i < a.length
   // MODIFIES a
   // EFFECTS: rearranges elements in array a so that some smallest element is at index i
   int j = minIndex(a); int t = a[j]; a[j] = a[i]; a[i] = t;    }
```

1.  Suppose we wish to transform the `setSmall` precondition `a != null`
    into defined behavior with an exception.
    1.  What Java exception would Bloch recommend for this
        transformation?

    2.  Rewrite the precondition and postcondition for `setSmall()` to
        achieve this result.

    3.  Does the given implementation of `setSmall()` satisfy this
        revised specification?
2.  Suppose we wish, in addition, to transform the `setSmall()`
    precondition `0 <= i < a.length` into defined behavior with an
    exception.
    1.  What exception would be recommended for this transformation?
        Hint: Note that `i` is described as an \"index\".

    2.  Extend your rewrite of the precondition and postcondition for
        `setSmall()` to achieve this result.

    3.  Does the given implementation of `setSmall()` satisfy this
        revised specification? Why? (Hint: it does not, and think about
        what exception raised in the specs vs. the implementation)

# Quiz 4: Immutable class

1.  Consider the following (supposedly) immutable class:

    ``` java
    public final class Immutable {
        private final String string;
        private final int x;
        private final List<String> list;

        public Immutable(String string, int x, List<String> list) {
            this.string = string;                     // Line A
            this.x = x;                               // Line B
            this.list = new ArrayList<String> (list); // Line C
        }

        public String getString() { return string; }  // Line D
        public int getInt()    { return x; }       // Line E
        public List<String> getList() { return list; }    // Line F
    }
    ```

    Which of the lines (A--F) has a problem wrt the immutability of
    class Immutable?

2.  For each of the above lines that has problem with immutability,
    write pseudocode code to demonstrate the issue

# Quiz 5: Iterator

The specification for Liskov\'s `elements()` method is given below.

-   Note 1: A Liskov Iterator has only the the `hasNext()` and `next()`
    methods.

    ``` java
    public Iterator elements()
    // EFFECTS: Returns a generator that will produce all the elements of
    //  this (as Integers), each exactly once, in arbitrary order.
    // REQUIRES: this must not be modified while the generator is in use


    ```

Consider the code below which uses `elements()`. Line numbers have been
added for reference purposes.

``` java
0: IntSet s = new IntSet();

1: s.insert(2);
2: s.insert(8);
3: Iterator itr = s.elements();
4: itr.next();
5: itr.next();
6: // See questions below
7: itr.next();

```

-   show the (stack) contents of `itr` after line 3


-   show the contents of `itr` after line 5.


-   If line 6 is `s.insert(12)`; show the contents of `itr` after line
    6?

# Quiz 6: Type

``` java
class A {
   public Iterator compose (Iterator itr)
   // Requires: itr is not null
   // Modifies: itr
   // Effects: if this is not appropriate for itr throw IAE
   // else return generator of itr composed with this
class B {
   public Iterator compose (Iterator itr)
   // Modifies: itr
   // Effects: if itr is null throw NPE
   // else if this is not appropriate for itr throw IAE
   // else return generator of itr composed with this
class C {
   public Iterator compose (Iterator itr)
   // Modifies: itr
   // Effects: if itr is null return iterator equal to this
   // else if this is not appropriate for itr throw IAE
   // else return generator of itr composed with this
```

Analyze the `compose()`{.verbatim} method in each of these cases
according to Liskov\'s Principle of Substitution. For each case, state
if the precondition and the postcondition parts are satisfied or fail,
and **justify**.

1.  B extends A.
2.  C extends A.
3.  A extends B.
4.  C extends B.
5.  B extends C.

# Quiz 7:

``` java
   Set<String> t = //  See questions below

   t.add("antelope");
   t.add("dog");
   t.add("cat");

// t.toString() is ???
```

1.  Suppose `t` is instantiated as
    `Set<String> t = new TreeSet<String>();`. At the end of the
    computation, what is `t.toString()?`

2.  Suppose `t` is instantiated as
    `Set<String> t = new TreeSet<String>((x,y) -> x.length() - y.length());`.
    At the end of the computation, what is `t.toString()?`

# Quiz 8:

Consider the following code:

``` java
public class Example <E> {
    String           string = "ant";
    Integer          seven = 7;
    E                e = null;
    Object[]         objects;
    List < Object >  listObject;
    List < E >       listE;
    public void m() {
          // Java code for questions appears here
    }
}
```

Independently consider the following 5 sequences of Java instructions.
For each sequence, what of the following choices will happen ? (i)
compiler warning; (ii) compiler error; (iii) runtime exception; or (iv)
normal run

-   

``` java
objects = new E[1];
objects[0] = e;
```

-   

``` java
listE = new ArrayList < E >();
listE.add(e);
listObject = listE;
```

-   

``` java
listObject = new ArrayList < String >();
listObject.add(string) ;
listObject.add(seven) ;
```

-   

``` java
objects = new Object[1];
objects[0] = string;
objects[0] = seven;
```

-   

``` java
objects = new String[1];
objects[0] = string;
objects[0] = seven;
```

# Quiz 9:

Consider the following code.

``` java
class Apple {
  // rep-inv:  name != null
  private String name;
  public Apple (String name) {
     if (name == null) throw new NPE(...);
     this.name = name;
  }
  @Override public boolean equals (Object o) {
     if (!(o instanceof Apple)) { return false; }
     Apple a = (Apple) o;
     return name.equals(a.name);
  }
  @Override public int hashCode() { // see questions below }
  @Override public String toString() { return name; }
}
class AppleTracker extends Apple {
  private static Set<String> inventory = new HashSet<String> ();
  public AppleTracker (String name) { super(name); inventory.add(name);}
  public static Set<String> getInventory() { return Collections.unmodifiableSet(inventory);}
}
// client code
Apple a = new Apple("Winesap");
AppleTracker at1 = new AppleTracker("Winesap");
AppleTracker at2 = new AppleTracker("Fuji");

```

Mark each of the following either **True** or **False**:

1.  The `equals()` method in the AppleTracker class is inherited from
    the Apple class.

-   `a.equals(at1)` sometimes returns true and sometimes returns false.
-   The `equals()` method in the Apple class relies on the rep-invariant
    to satisfy its contract.
-   `a.equals(at1)` and `at1.equals(a)` are both true.
-   `a.equals(at2)` and `at2.equals(a)` are both false.
-   `at1.equals(a)` and `a.equals(at2)` are both true, but
    `at1.equals(at2)` is false.
-   It would correct to implement `hashCode()` as
    `return name.hashCode();`
-   It would correct to inherit `hashCode()` from the Object class.
-   Bloch would object to replacing `o instanceof Apple` with a
    predicate built atop `getClass()`.

# Quiz 10:

Consider the following Java code, and suppose the main method in `Sub`
is executed.

``` java
public class Super {
  private String y;
  public Super () { stut();}
  public void stut() { if (y == null) {y = "cat";} else {y = y + y;}}
}
public class Sub extends Super {
  private String x;
  public Sub (String s) { x = s;}
  @Override public void stut() {
     x = x + x;
  }
  public static void main(String[] args) {
      Super s = new Sub("dog");
  }
}
```

1.  Is the constructor in Super invoked? Why or why not?

2.  Is the stut() method in Super invoked? Why or why not?

3.  Is the stut() method in Sub invoked? Why or why not?

4.  Based on this example, what rule do you come up with for invoking
    methods in constructors? -->
<!-- -->
