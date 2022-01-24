// Subclass of Point with standard recipes for equals, hashCode
// Breaks symmetry
class SubPoint extends Point {
   private int y;
   public SubPoint (int x, int y) { super(x); this.y = y; }

   @Override public boolean equals(Object o) {
      return (o instanceof SubPoint) &&
              super.equals(o) &&
              y == ((SubPoint) o).y;
   }

   @Override public int hashCode() {
      int result = 17;
      result = 31 * result + super.hashCode();
      result = 31 * result + y;
      return result;
   }

   @Override public String toString() {
      return super.toString() + ";y " + y;
   }

}
