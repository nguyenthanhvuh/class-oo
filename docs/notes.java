public class User {
    private String name;
    public User (String name) { this.name = name; }
    @Override public boolean equals (Object obj) {
        if (!(obj instanceof User)) return false;
        return ((User) obj).name.equals(this.name);
    }
    // other methods omitted
}

User u = new User("Vu");

// go to Javadoc  equal


u.equals(u);  //should be true true (javadoc), and it is true (because that's what the code does). So this particular scenario, it satisfies/complies wit the java doc contract

u.equals(null); //should be false (javadoc), and is false (because the code as null is not an instance of user)..

u.equals("Vu"); //should be false(javadoc), and is false (code instancesof User returns false)

User v = new User(null);  // what about this?  this is ok (implicit cast)

v.equals(u);  // sould be false, and is
//return ((User) obj)."Vu".equals(null);
//- string equal method "Vu".equals ... returns False.  

u.equals(v);
// v is an instance so can cast,  then dereference ((User) obj).name.equals , i.e., null.equals,  which cause NPE.
// this is WRONG because it breaks a contract,  it should return FALSe but here it gives a null pointer


/*
What can we do?  
- we can disallow null names in the constructor  

e.g.,  public User(string name){if (name == null) throw new NPE() ; ..

- note might not be the best practice,  but it allows us to satisfies contract


- can also change the equals code
   // check if ((User) obj).name == null, then return false

 */



public class SpecialUser extends User {
    private int id;
    public SpecialUser (String name, int id) { super(name); this.id = id; }
    @Override public boolean equals (Object obj) {
        if (!(obj instanceof SpecialUser)) return false;
        return super.equals(obj) && ((SpecialUser) obj).id == this.id;
    }
    // other methods omitted
}   
     
   
// will not spend lots of time here because we will use this later in the semester.
// what properties are broken ?  not symmetric .. You try it out.  We won't do it now.  Try it before reading Bloch 10,  it will talk about some of these.   More challenging due to inheritance.

// know the first part,  not the second part

