/*
 * MapPoly:  Liskov's Poly class, converted to a (Tree)Map rep.
 * Notes:
 *   0) Relies on TreeMap (not just Map) for efficiently finding max nonzero coefficient
 *   1) Private constructor not useful, so deleted
 *   2) No-arg constructor implemented with 2-arg constructor
 *   3) Empty map represents the 0 MapPoly (very different from Poly)
 *   4) Uses TreeMap descending iterator to find degree(); hence no deg variable
 *   5) Code generally shorter.
 */
import java.util.*;

public class MapPoly {

    private TreeMap<Integer, Integer> trms;

    // Effects: Initializes this to be the zero polynomial
    public MapPoly() {
       this(0,0);
    }

    // Effects: If n < 0 throws IllegalArgumentException
    // else initializes this to be the polynomial c*x^n
    public MapPoly(int c, int n) throws IllegalArgumentException {
       if (n < 0) {
          throw new IllegalArgumentException("MapPoly(int, int) constructor");
       }
       trms = new TreeMap<Integer, Integer> ();
       if (c != 0) { trms.put(n, c); }
    }

    // Effects: returns the degree of this
    public int degree() {
       int result  = 0;
       if (trms.size() > 0) {
          result = trms.descendingKeySet().iterator().next();
       }
       return result;
    }

    // Effects: returns the coefficent of the term of this whose exponent is d
    public int coeff(int d) {
       if (d < 0) throw new IllegalArgumentException("MapPoly.coeff");
       if (trms.containsKey(d)) return trms.get(d);
       return 0;
    }

    // Effects: If q is null throw NullPointerException
    // else return the MapPoly this - q
    public MapPoly sub(MapPoly q) {
       return add(q.minus());
    }

    // Effects: return the MapPoly -this
    public MapPoly minus() {
       MapPoly result = new MapPoly();
       for (Integer i : trms.keySet()) {
          result.trms.put (i, -trms.get(i));
       }
       return result;
    }

    // Effects: If q is null throw NullPointerException
    // else return the MapPoly this + q
    public MapPoly add(MapPoly q) {
       
       // find all the nonzero coefficients in either this or q
       Set<Integer> nonZero = new HashSet<Integer>(q.trms.keySet());
       nonZero.addAll(trms.keySet());

       // Add the coefficients together; store the nonzero results
       MapPoly result = new MapPoly();
       for (Integer i : nonZero) {
          int newCoeff = coeff(i) + q.coeff(i);
          if (newCoeff != 0) result.trms.put(i, newCoeff);
       }
       return result;
    }

    // Effects: If q is null throw NullPointerException
    // else return the MapPoly this * q
    public MapPoly mul(MapPoly q) {
       MapPoly result = new MapPoly();

       for (Integer i:  trms.keySet()) {
          for (Integer j:  q.trms.keySet()) {
              result = result.add(new MapPoly (coeff(i) * q.coeff(j), i+j));
          }
       }
       return result;
    }

    @Override public String toString() {   // Note that TreeMap gets the order right
       String r = "MapPoly:";

       if (trms.size() == 0) {   // special case for empty Map
           r += " " + 0;
       }

       for (Integer i: trms.keySet()) {
          if (coeff(i) < 0) { r += " - " + -coeff(i) + "x^" + i; }
          else              { r += " + " +  coeff(i) + "x^" + i; }
       }
       return r;
    }

    public static void main(String[] args) { 
       System.out.println("Hello");
       MapPoly mp = new MapPoly();
       System.out.println("MapPoly mp = " + mp);
       mp = mp.add(new MapPoly(3,5));
       System.out.println("MapPoly mp = " + mp);
       mp = mp.add(new MapPoly(-3,5));
       System.out.println("MapPoly mp = " + mp);
       mp = mp.add(new MapPoly(-3,5));
       System.out.println("MapPoly mp = " + mp);
       mp = mp.add(new MapPoly(-2,2));
       System.out.println("MapPoly mp = " + mp);
       System.out.println("MapPoly -mp = " + mp.minus());
       System.out.println("MapPoly mp*mp = " + mp.mul(mp));
    }
}
