11/15

In-class 9B

```java
public class IntSet implements Cloneable {  
    private List<Integer> els;
    public IntSet () { els = new ArrayList<Integer>(); }
    ...
    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof IntSet)) return false;

        IntSet s = (IntSet) obj;
        

    for (Integer i : s.els){
       if (!els.contains(i)){
         return false;
        }
    }

    for (Integer i: els){
       if(!s.els.contains(i)){
          return false;
      }
    }        


    @Override
    public int hashCode() { 
        // see below 
    }

    // adding a private constructor
    private IntSet (List<Integer> list) { els = list; }

    @Override 
    public IntSet clone() { 
        return new IntSet ( new ArrayList<Integer>(els));
    }

}
```




Improper class inheritence would cause problem of encapsulation





Consider Bloch's InstrumentedHashSet, InstrumentedSet, and ForwardingSet examples:
```java
public class InstrumentedHashSet<E> extends HashSet<E>{
    private int addCount = 0;   
    public InstrumentedHashSet() {}

    @Override public boolean add(E e){ 
        addCount++; 
        return super.add(e); 
    }
    @Override public boolean addAll(Collection<? extends E> c){ 
        // What to do with addCount?
        return super.addAll(c); 
    }
    public int getAddCount(){ return addCount; }
}



public class InstrumentedSet<E> extends ForwardingSet<E>{
    private int addCount = 0;   

    public InstrumentedSet(Set<E> s){ super(s); }
    @Override public boolean add(E e){ addCount++; return super.add(e); }
    public int getAddCount(){ return addCount; }
}
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> s;

    public ForwardingSet(Set<E> s){ this.s = s; }
    public           boolean add(E e)        { return s.add(e);     }
    public           boolean remove(Object o){ return s.remove(o);  }
    @Override public boolean equals(Object o){ return s.equals(o);  }
    @Override public int     hashCode()      { return s.hashCode(); }
    @Override public String  toString()      { return s.toString(); }
    // Other forwarded methods from Set interface omitted
}

//Consider also the following client code:

Set<String> r = new HashSet<String>();
r.add("ant"); r.add("bee");

Set<String> sh = new InstrumentedHashSet<String>();
sh.addAll(r);

Set<String> s =  new InstrumentedSet<String>(r);
s.add("ant"); s.add("cat");

Set<String> t = new InstrumentedSet<String>(s);
t.add("dog");

r.remove("bee");
s.remove("ant");
```


How do you think the addCount variable should be updated in the addAll() method in InstrumentedHashSet?
Why is this a hard question?
What does the answer say about inheritance?
Does equals() behave correctly in InstrumentedHashSet?
Given your previous answer, what is the value of sh.addCount at the end of the computation?
Consider the InstrumentedSet solution. Besides being correct (always a plus!) why is it more general than the InstrumentedHashSet solution?
At the end of the computation, what are the values of: r, s, and t?
What would a call to s.getAddCount() return at the end of the computation?
At the end of the computation, what are the values of: r.equals(s), s.equals(t), and t.equals(s)?
Are there any problems with the equals() contract?
Would this still work if you globally replaced sets with lists?
Would this still work if you globally replaced sets with collections?

Note: There is a lot going on in this example. I highly recommend that you play with the code until you understand it.
















```java
  import java.util.*;


  public class IntSet implements Cloneable {  
     private List<Integer> els;

     @Override public boolean equals(Object obj) { 
        if (!(obj instanceof IntSet)) return false;

        IntSet s = (IntSet) obj;
        for (Integer i : s.els){
            if (!els.contains(i)){
                return false;
            }
        }

        for (Integer i: els){
            if(!s.els.contains(i)){
                return false;
            }
        }


        return true;
     }

     @Override public int hashCode() { 
        // see below 
        return 42;
     }

     public IntSet () { els = new ArrayList<Integer>(); }

     private IntSet (List<Integer> list) { els = list; }

     @Override public IntSet clone() { 
        return new IntSet (new ArrayList<Integer>(els));
     }
  }
```




** Reflection
- Bloch discusses specific rules for making a class immutable. Did you find any of these rules confusing?
- Bloch's InstrumentedHashSet example demonstrates how inheritance can break encapsulation. Does the JavaDoc for HashSet, Set and/or Collection follow the Bloch's Item 19 advice for documenting for inheritances?
- Bloch's InstrumentedSet example has a lot going on in it. What aspects, if any, of this example did you find confusing? 

** Lecture

**** Make Each class or Member as Inaccessible as Possible (Slide 4)
    - private
    - package-private
    The above 2 are preferred, developer's ..  
    - protected for subclass
    - public
    These two are essentially public (anyone can subclass)


**** Item 17 (Slide 9)
     - show all the benefits on the slide
     - 


## In-class 10A

```java
public class InstrumentedHashSet<E> extends HashSet<E>{
    private int addCount = 0;   
    public InstrumentedHashSet() {}

    @Override public boolean add(E e){ 
        addCount++; 
        return super.add(e); 
    }
    @Override public boolean addAll(Collection<? extends E> c){ 
        // What to do with addCount?
        return super.addAll(c); 
    }
    public int getAddCount(){ return addCount; }
}



public class InstrumentedSet<E> extends ForwardingSet<E>{
    private int addCount = 0;   

    public InstrumentedSet(Set<E> s){ super(s); }
    @Override public boolean add(E e){ 
        addCount++; 
        return super.add(e); 
    }
    public int getAddCount(){ return addCount; }
}
public class ForwardingSet<E> implements Set<E> {
    private final Set<E> s;

    public ForwardingSet(Set<E> s){this.s = s;}
    public           boolean add(E e)        { return s.add(e);     }
    public           boolean remove(Object o){ return s.remove(o);  }
    @Override public boolean equals(Object o){ return s.equals(o);  }
    @Override public int     hashCode()      { return s.hashCode(); }
    @Override public String  toString()      { return s.toString(); }
    // Other forwarded methods from Set interface omitted
}

Consider also the following client code:

Set<String> r = new HashSet<String>();
r.add("ant"); r.add("bee");
//r : [ant, bee]  

Set<String> sh = new InstrumentedHashSet<String>();
sh.addAll(r);
//sh: [ant, bee]
//getCount = 2

Set<String> s =  new InstrumentedSet<String>(r);
s.add("ant"); s.add("cat");
//s: [ant, bee, cat]
//r: [ant, bee, cat]   s.add calls r.add

Set<String> t = new InstrumentedSet<String>(s);
t.add("dog");   //s.add calls r.add
//s: [ant, bee, cat, dog]   
//t: [ant, bee, cat, dog]
//r: [ant, bee ,cat, dog]

r.remove("bee");
//s: [ant, cat, dog]   
//t: [ant, cat, dog]
//r: [ant, cat, dog]
s.remove("ant");
//s: [cat, dog]   
//t: [cat, dog]
//r: [cat, dog]
//s.addCount() = 3
//t.addCount() = 1
```

- How do you think the addCount variable should be updated in the addAll() method in InstrumentedHashSet?
    A: no, just leave everything, let dynamic dispatching make the call to add().  If we try to do something here it might double count (e.g., in the Bloch's example in the book)
    - Why is this a hard question?
        A: depends a lot on implementation details, we need to know how Add works etc to determine we should or should not do things to avoid double count
    - What does the answer say about inheritance?
        A: it breaks encapsulation
    - Does equals() behave correctly in InstrumentedHashSet?
        A: yes, it inherits equals from HashSet (which probably inherits from Set) and therefore does the correct containment checking for set equivalence.

- Given your previous answer, what is the value of sh.addCount() at the end of the computation?
A: 2

- Consider the InstrumentedSet solution. Besides being correct (always a plus!) why is it more general than the InstrumentedHashSet solution?
    A: This is item 18: favor composition over inheritence:  benefits include robust, flexible, doesn't break encapsulation etc ... 
- At the end of the computation, what are the values of: r, s, and t?
    A: all just [cats, dogs]  because they all reference the same Hashset
What would a call to s.getAddCount() return at the end of the computation?
    A: s.addCount() == 3 because we call s.add() 3 times ;  t.addCount() = 1 because we call t.add() 1 time

- At the end of the computation, what are the values of: r.equals(s), s.equals(t), and t.equals(s)?
    - A: all true (which is correct, because these are all equivalent sets)
    - Are there any problems with the equals() contract?
      A: no, should be ok here.  
- Would this still work if you globally replaced sets with lists?
    A: in general yes and no , rely on equal of list (if you expect list equality then it is correct, but if you expect set equality then it doesn't)
- Would this still work if you globally replaced sets with collections?
    A: same answer, same reason ,  rely on equal of different collections 


Reminder:

- schedule next week
- quiz/exam no collaboration 


- [bat, cat, dog] :  like a stack,  next : pop 


List<String> list = new List<>();
list.add("bat");
list.add("cat");
list.add("dog");

Iterator<String> itr = list.iterator();
// iter: [bat, cat, dog]   #can think of this as stack

itr.next(); //return bat
// itr: [cat, dog]

itr.hasNext(); // return true
// iter: [cat, dog]

list.add("element")
// list: [bat, cat, dog, elephant]
// itr: undefined (according to Iterator interface, e.g., the Iterator elements() in class Liskov's IntSet, which requires elements not being modified while generator being used )
// made the states undefined, so calling iter still do something, but not specified.

itr.next(); // undefined behavior 
iter.next(); // undefined behavior 


Q: add a `prev` method, allows us to go back and forth 
// use 2 stacks
next()
previous()

List<String> list = new List<>();
list.add("bat");
list.add("cat");
list.add("dog");

Iterator<String> itr = list.iterator();  //itr.P = []  , itr.N = [bat,cat,dog] 
itr.prev()                          // get exception
itr.next()                          //itr.P = [bat], itr.N = [cat, dog]
itr.next()                          //itr.P = [cat,bat]  Notice cat is pushed on the top, itr.N = [dog]
itr.prev();                         //itr.P = [bat], itr.N =[cat,dog]
itr.next();                         //itr.P = [cat,bat],  itr.N=[dog]
itr.next();                         //itr.P = [dog,cat,bat], itr.N = []
itr.prev();                         //itr.P = [cat,bat], itr.N = [dog]
itr.prev();                         //itr.P = [bat], itr.N =[cat, dog]


Q: add remove
Iterator<String> itr = list.iterator();  //itr.P = []  , itr.N = [bat,cat,dog] 
itr.next()                          // itr.N = [cat, dog]; return b
itr.remove()                        // list = [c,d]; itr = [c,d]
itr.remove()                        // Illegal State Exception; itr = [c,d]

// need to keep track if next has been called 


Q: immutable iterator
//Java doesn't support this, we just use this to understand Immutability

public interface IIterator<E>{}
    public boolean hasNext();  // no change
    //public E next()   =>  split into nextIterator and nextE
    public Iterator nextIterator()
    public E nextE()
}

list = ... // [b,c,d]
itr = list.IIterator();     // itr = [b,c,d]
itr.nextE();   // return b; itr = [b,c,d] 
itr.nextIterator();  // return IIterator with state [c,d], itr = [b,c,d]
itr.nextIterator();  // return IIterator with state [c,d], itr = [b,c,d]
...  not good,  what am I missing?

well I need 
itr.nextE();   // return b; itr = [b,c,d] 
itr = itr.nextIterator(); // return IIterator w/ state [c,d]; itr = [c,d] 
itr.nextE();   // return c; itr = [c,d]

// should we have a remove method in an immutable iterator ?
// No: because if call remove twice, 

itr.remove() // take c out
itr.remove() // do something else ,  but this is problematic because itr is immutable so it should always behave the same way. 

Inclass Exercise 4B
- Focus on #3 (relevant to hw assignment)

public final class Period {               // Question 3
    private final Date start;
    private final Date end;

    /**
     * @param start the beginning of the period
     * @param end the end of the period; must not precede start
     * @throws IAE if start is after end
     * @throws NPE if start or end null
     */

    public Period (Date start, Date end) {
        if (start.compareTo(end) > 0) throw new IAE();
        this.start = start; this.end = end;  // Question 1
    }
    public Date start() { return start;}    // Question 2
    public Date end()   { return end;}      // Question 2


removing final ->  now immutable, can now subtype , extends 
note students want to just access variables, no cannot access them because they are *private*
but override method is enough to break this 


public class MyClass extends Period{
    private Date myDate = new Date(0)

@override public Date start(){
    if (itsTime()){
        return myDate;  // this is mutable !
    }
    else{
        return super.start()
    }

}

public class LoanProvider{
    Period p;

    public LoanProvider (Period p, other stuff){
        this.p = p ; // no defense copy, Because Period is immutable 
    }
}

Period m = new myClass();  //use start method from my class and hence when itsTime() will use myDate defined in my class,  not the start in Period.  
LoanProvider lp = new LoanProvider(m, ...) // will have start from myClass
