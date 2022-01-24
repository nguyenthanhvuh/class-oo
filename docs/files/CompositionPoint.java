// Class composed over Point with standard recipes for equals, hashCode
// Satisfies equals, hashCode contracts
class CompositionPoint {
   private Point p;   // Composition variable
   private int y;

   public CompositionPoint (int x, int y) { p = new Point(x); this.y = y; }

   @Override public boolean equals(Object o) {
      if (!(o instanceof CompositionPoint))
        return false;
      CompositionPoint cp = (CompositionPoint) o;
      return p.equals(cp.p) && cp.y == y;
   }

   @Override public int hashCode() {
      int result = 17;
      result = 31 * result + p.hashCode();
      result = 31 * result + y;
      return result;
   }

   @Override public String toString() {
      return p + ";y " + y;
   }

}
