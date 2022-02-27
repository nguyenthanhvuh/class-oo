public class User {
    private String name;

    //precond :  name cannot null
    public User (String name) { if name == null {}...;  this.name = name; }
    
    @Override public boolean equals (Object obj) {
        if (!(obj instanceof User)) return false;
        return ((User) obj).name.equals(this.name);
    }
    // other methods omitted
}

User u = new User("Vu");

u.equals(u); //contract: return true, implementation: return true 
u.equals(null);  // contract: return False ; implementation: return false
u.equals("Vu"); // contract return False,  implementation : return False


User v = new User(null); 
v.equals(u); //contract: false;  implementation: returns False
u.equals(v);// contract: false;    implemenation: raise NPE



public class SpecialUser extends User {
    private int id;
    public SpecialUser (String name, int id) { super(name); this.id = id; }
    @Override public boolean equals (Object obj) {
        if (!(obj instanceof SpecialUser)) return false;
        return super.equals(obj) && ((SpecialUser) obj).id == this.id;
    }
    // other methods omitted
}   
     




void remove() 

// Removes from the underlying collection the last element returned by this iterator (optional operation). This method can be called only once per call to next(). The behavior of an iterator is unspecified if the underlying collection is modified while the iteration is in progress in any way other than by calling this method.

//   Throws:
//   - UnsupportedOperationException - if the remove operation is not supported by this iterator
//   - IllegalStateException - if the next method has not yet been called, or the remove method has already been called after the last call to the next method


    f(x,y):
//precond:  y != 0
    if y == 0: ...
     return x/y
