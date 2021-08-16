import java.util.*;

public class StackInClass {
   private Object[] elements; private int size = 0;

   public StackInClass() { this.elements = new Object[0]; }

   public void push (Object e) {
     if (e == null) throw new NullPointerException("Stack.push");
     ensureCapacity(); elements[size++] = e;  
   }

   public void pushAll (Object[] collection) { for (Object obj: collection) { push(obj); } }

   public Object pop () {
     if (size == 0) throw new IllegalStateException("Stack.pop");
     Object result = elements[--size];
     // elements[size] = null;
     return result;
   }

   @Override public String toString() {
      String result = "size = " + size;
      result += "; elements = [";
      for (int i = 0; i < elements.length; i++) {
         if (i < elements.length-1)
            result = result + elements[i] + ", ";
         else
            result = result + elements[i];
      }
      return result + "]";
   }
  private void ensureCapacity() {
      if (elements.length == size) {
         Object oldElements[] = elements;
         elements = new Object[2*size + 1];
         System.arraycopy(oldElements, 0, elements, 0, size);
      }
   }
}
