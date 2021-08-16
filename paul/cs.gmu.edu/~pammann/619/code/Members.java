import java.util.*;

public class Members {
    // Members is a mutable record of organization membership
    // AF: Collect the list as a set
    // rep-inv1: members != null
    // rep-inv2: members != null && no duplicates in members
    // for simplicity, assume null can be a member...

    List <Person> members;   // the representation

    //  Post: person becomes a member
    public void join (Person person) { members.add   (person);}

    //  Post: person is no longer a member
    public void leave(Person person) { members.remove(person);}

    //  Post: returns true iff person is a member
    public boolean isMember(Person person) { return members.contains(person);}
}
class Person {}
