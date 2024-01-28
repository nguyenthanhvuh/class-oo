#!/usr/bin/env python3

class User:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
            #None.__eq__("Marry)
        return self.name.__eq__(other.name)


implies = lambda p, q: not p or q # =>


u1 = User("Mary")
u2 = User("John")
u3 = User("Tony")

u1a = User("Mary")
u1b = User("Mary")

print("Reflexive: a.__eq__(a)")
print(u1.__eq__(u1))                      # impl: True,  Contract: True

print("Symmetry:  a == b <=> b == a")
print(u1.__eq__(u1a), u1a.__eq__(u1))     # impl: True, Contract: True
print(u1.__eq__(u2), u2.__eq__(u1))     # impl: False, Contract: False

print ("Transitive: a == b and b == c implies a == c")

# # (u1 == u1a) and (u1a == u1b) implies (u1 == u1b)
# #  impl: True, Contract: True

print(implies(u1.__eq__(u1b) and u1b.__eq__(u1a), u1.__eq__(u1a)))

# # (u1 == u2) and (u2 == u3) implies u1 == u3
# # impl: True, Contract: True

# print(implies(u1.__eq__(u2) and u2.__eq__(u3), u1.__eq__(u3)))


print("Special cases")
# uNone = User(None)
# print(u1.__eq__(uNone))                             # impl: False, Contract: False
# print(uNone.__eq__(u1))                             # impl: False, Contract: False


# uNumber = User(1)
# print(u1.__eq__(uNumber)) # impl: False, Contract: False
# print(uNumber.__eq__(u1)) # impl: False, Contract: False

# # INHERITANCE

class SuperUser(User):
    def __init__(self, name, nid):

        super().__init__(name)
        self.nid = nid

    def __eq__(self, other):

        if not isinstance(other, SuperUser):
            if isinstance(other, User):
                return other.__eq__(self)
            return False

        return super().__eq__(other) and self.nid == other.nid

s1 = SuperUser("Mary", 1)
print(s1.__eq__(u1))  # False
print(u1.__eq__(s1))  # True









# print("Symmetry:  a.__eq__(b) implies b.__eq__(a)")
# print(implies(u1.__eq__(s1), s1.__eq__(u1)))  # impl: False, Contract: True
# print(u1.__eq__(s1))  # True
# print(s1.__eq__(u1))  # but this is False
