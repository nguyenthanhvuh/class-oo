import org.junit.*;
import org.junit.runner.RunWith;
import static org.junit.Assert.*;
import static org.junit.Assume.*;

import org.junit.experimental.theories.DataPoint;
import org.junit.experimental.theories.DataPoints;
import org.junit.experimental.theories.Theories;
import org.junit.experimental.theories.Theory;

import java.util.*;

@RunWith(Theories.class)
public class PointTheoryTest {

   @DataPoints
   public static Object[] points = {
      null,
      new Point(1),
//      new Point(2),
      new CompositionPoint(1,2),
      new CompositionPoint(1,3)
   };


   @Theory public void symmetryTest( Object p1, Object p2) {
      System.out.println("In Symmetry Test: p1, p2: " + p1 + ", " + p2);

      assumeTrue (p1 != null);      // Precondition
      assumeTrue (p2 != null);      // Precondition
      assertTrue (p1.equals(p2) == p2.equals(p1));   // Postcondition
    }

   @Theory public void transitivityTest(Object p1, Object p2, Object p3) {
      System.out.println("In Transitivity Test: p1, p2, p3: " + p1 + ", " + p2 + ", " + p3);

      assumeTrue (p1 != null);      // Precondition
      assumeTrue (p2 != null);      // Precondition
      assumeTrue (p3 != null);      // Precondition
      assumeTrue (p1.equals(p2) && p2.equals(p3));   // Precondition
      System.out.println("Passed assumption");
      assertTrue (p1.equals(p3));   // Postcondition
    }

   @Theory public void hashCodeEqualsConsistency( Object p1, Object p2) {
      System.out.println("In hashCodeEqualsConsistency Test: p1, p2: " + p1 + ", " + p2);

      assumeTrue (p1 != null);      // Precondition
      assumeTrue (p2 != null);      // Precondition
      assumeTrue (p1.equals(p2));   // Precondition
      System.out.println("Passed assumption");
      assertTrue (p1.hashCode() == p2.hashCode());   // Postcondition
    }

}


