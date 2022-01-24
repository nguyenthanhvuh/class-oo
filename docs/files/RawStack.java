/**
  * Bloch's Stack example without generics
  */

import java.util.*;

public class RawStack {

   private Object[] elements;
   private int size = 0;


   public RawStack() {
     this.elements = new Object[0];
   }

   public void push (Object e) {
     ensureCapacity();
     elements[size++] = e;
   }

   public Object pop () {
     if (size == 0) throw new IllegalStateException("RawStack.pop");
     Object result = elements[--size];
     elements[size] = null;    // Eliminate obsolete reference
     return result;
   }

   private void ensureCapacity() {
      if (elements.length == size) {
         Object oldElements[] = elements;
         elements = new Object[2*size + 1];
         System.arraycopy(oldElements, 0, elements, 0, size);
      }
   }

}
