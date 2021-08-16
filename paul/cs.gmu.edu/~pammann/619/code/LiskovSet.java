import java.util.*;
/*
 * Liskov's IntSet example (called LiskovSet), with minor changes
 * This version doesn't include AF or RI
 */

public class LiskovSet {

  // Overview:  LiskovSets are unbounded, mutable sets of integers
  private List<Integer> els;    // the rep
  
  // constructor
  // EFFECTS:  Intitializes this to be empty
  public LiskovSet () { els = new ArrayList<Integer>(); }

  // methods
  // MODIFIES this
  // EFFECTS:  Adds x to the elements of this
  public void insert (int x) {
     if (els.indexOf(x) < 0)    // could also self-use isIn()
     els.add(x);
  }

  // MODIFIES this
  // EFFECTS:  Removes x from this
  public void remove (int x) {
     int index = els.indexOf(x);
     if (index < 0) return;
     els.set(index, els.get(els.size()-1));
     els.remove(els.size()-1);
  }
  
  // EFFECTS:  Returns true if x is in this else returns false
  public boolean isIn (int x) {
     return els.indexOf(x) >= 0;      // could also use contains()
  }

  // EFFECTS:  Returns the cardinality of this
  public int size () {
     return els.size();
  }

  // EFFECTS:  If this is empty throw IllegalStateException
  //           else returns an arbitrary element of this
  public int choose () {
     return els.get(els.size()-1);
  }
}
