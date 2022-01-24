import java.util.*;

public final class Complex {
   private final double re;
   private final double im;

   public Complex (double re, double im) {
       this.re = re;
       this.im = im;
   }

   // Accessors with no corresponding mutators
   public double realPart()      { return re; }
   public double imaginaryPart() { return im; }

   public Complex add (Complex c ) {
      return new Complex (re + c.re, im + c.im);
   }

   public Complex subtract (Complex c ) {
      return new Complex (re - c.re, im - c.im);
   }

   public Complex multiply (Complex c ) {
      return new Complex (re * c.re - im * c.im,
                          re * c.im + im * c.re);
   }

   public Complex divide (Complex c ) {
      double tmp = c.re * c.re + c.im * c.im;
      return new Complex ((re * c.re - im * c.im) / tmp,
                          (re * c.im + im * c.re) / tmp);
   }

   @Override public boolean equals (Object o) {
     if (o == this)               return true;
     if (!(o instanceof Complex)) return false;
     Complex c = (Complex) o;

     // See Bloch page 43 to find out why to use compare() instead of ==
     return Double.compare(re, c.re) == 0 &&
            Double.compare(im, c.im) == 0;
   }

   @Override public int hashCode () {
      int result = 17 + hashDouble(re);
      result = 31 * result + hashDouble(im);
      return result;
   }

   private int hashDouble (double val) {
      long longBits = Double.doubleToLongBits(val);
      return (int) (longBits ^ (longBits >>>32));
   }

   @Override public String toString() {
      return "(" + re + " + " + im + "i)";
   }


   public static void main(String[] args) {
      Complex c1 = new Complex (2, 3);
      Complex c2 = new Complex (4, 5);
      System.out.println("c1           : " + c1);
      System.out.println("c2           : " + c2);
      System.out.println("c1 + c2      : " + c1.add(c2));
      System.out.println("c1 - c2      : " + c1.subtract(c2));
      System.out.println("c1 * c2      : " + c1.multiply(c2));
      System.out.println("c1 / c2      : " + c1.divide(c2));
      System.out.println("c1.equals(c2): " + c1.equals(c2));
      System.out.println("c1.hashCode(): " + c1.hashCode());
   }

}
