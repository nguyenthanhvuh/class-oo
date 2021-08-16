import java.util.*;
import java.util.concurrent.*;

// Bloch's initial version
public class Chooser {
   private final Object[] choiceArray;

   public Chooser (Collection choices) {
      choiceArray = choices.toArray();
   }

   public Object choose() { 
      Random rnd = ThreadLocalRandom.current();
      return choiceArray [rnd.nextInt(choiceArray.length)];
   }
}
