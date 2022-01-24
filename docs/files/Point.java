//  Class to illustrate equals() contract demos
public class Point {

   private int x;

   public Point (int x) { this.x = x; }

   @Override public boolean equals(Object o) {
      return (o instanceof Point) &&
              x == ((Point) o).x;
   }

   @Override public int hashCode() {
      int result = 17;
      result = 31 * result + x;
      return result;
   }

   @Override public String toString() {
      return "x " + x;
   }
}
