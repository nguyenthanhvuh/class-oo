import java.util.*;

// Bloch's Broken Immutable time period class
public final class Period {               
  private final Date start;
  private final Date end;

  /**
    * @param start the beginning of the period
    * @param end the end of the period; must not precede start
    * @throws IAE if start is after end
    * @throws NPE if start or end null
    */

  public Period (Date start, Date end) {
    if (start.compareTo(end) > 0) throw new IllegalArgumentException();
    this.start = start; this.end = end;  
  }
  public Date start() { return start;}   
  public Date end()   { return end;}     
}
