/**
  * Generic Queue example
  * Mutable Version, without specifications
  * SWE 619
  * @author Paul Ammann
  */

import java.util.*;

public class Queue <E> {

   private List<E> elements;
   private int size;

   public Queue() {   
      this.elements = new ArrayList<E>();
      this.size = 0;
   }

   public void enQueue (E e) {
     elements.add(e);
     size++;
   }

   public List<E> enQueue_Immutable(E e){
       List<E> new_elements = copy(elements); 
        new_elements.add(e);
        return new_elements;
    }


   public E deQueue () {
     if (size == 0) throw new IllegalStateException("Queue.deQueue");
     E result = elements.get(0);
     elements.remove(0);
     size--;
     return result;
   }

    public List<E> deQueue_Immutable(){
        if (size == 0) throw new IllegalStateException("Queue.deQueue");
        List<E> new_elements = copy(elements);
        new_elements.remove(0);
        return new_elements;
    }

    public E getFirst(){
        if (size == 0) throw new IllegalStateException("Queue.deQueue");
        return elements.get(0);
    }

   public boolean isEmpty() {
      return size == 0;
   }

       
  public static void main(String[] args) {
     // Simple exercise to enQueue/deQueue cmd line args
     // Usage:  java Queue item1 item2 item3 ...
     Queue <String> q = new Queue <String>();
     for (String arg : args)
        q.enQueue(arg);
     while (!q.isEmpty() )
        System.out.println(q.deQueue());

  }

}
