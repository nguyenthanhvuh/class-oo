import java.util.*;

public class IntSet implements Cloneable {  
   private List<Integer> els;

   @Override public boolean equals(Object obj) { 
      if (!(obj instanceof IntSet)) return false;

      IntSet s = (IntSet) obj;
      /// ???
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
