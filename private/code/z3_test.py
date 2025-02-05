from z3 import *    # import all Z3 functions

# some good examples here https://hanielbarbosa.com/papers/fm2024.pdf


# check that Z3 works
x = Int('x')
y = Int('y')
solve(x > 2, y < 10, x + 2*y == 7)
# [y = 0, x = 7]


# Propositional logic
a, b, c = Bools('a b c')

solve(a)   # [a = True]
solve(a == b, a == Not(b)) # [No solution]

prove(a == a) # True

prove(Implies(a, a)) # True (a => a)
prove (Implies(a, b)) # False (a => b)
prove(Implies(a, b) == Or(Not(a), b)) # implication a => b  == !a or b
prove (Not(And(a, b)) == Or(Not(a), Not(b))) # De Morgan !(a and b) == !a or !b
prove(Implies(a, b) == Implies(Not(b), Not(a))) # contraposition a => b == !b => !a


prove(Implies(And(a, Implies(a, b)), b)) # #modus ponens  a, a => b => b

# Using SOLVE instead of PROVE
# if a is valid, then prove(a) returns True and solve(Not(a)) return unsat
solve(Not(Implies(a,a)))


# if a is invalid, then prove(a) returns False and solve(Not(a)) returns an assignment (or counterexample)
solve(Not(Implies(a,b)))



# Using SOLVER 
# modus ponens

s = Solver()
s.add(a)            #a is true
s.add(Implies(a,b)) # a => b
s.add(Not(b))       #but b is false
print('modus ponens', s.check())  #unsat -> not possible




# VARIOUS EXAMPLES

### Equivalence
prove(x ==x)   ### reflexivity
prove(Implies(a == b,b == a)) ### symmetric
prove(Implies(And(a == b, b == c), a == c)) ### transitive


# Arithmetic (first order logic)
x, y = Ints('x y')
prove(x + y == y + x) # commutativity
prove(Implies(x > 10, x > 5)) # stronger
prove(Implies(x==3, Or(x == 5, x == 3)))
prove(Implies(x*x == 25, Or(x == 5, x == -5)))

# If all humans are mortal and Soacrates is human, then Socrates is mortal
Human = DeclareSort('Human')
x = Const('x', Human)
Socrates = Const('Socrates', Human)
Mortal = Function('Mortal', Human, BoolSort()) # function that takes a human and returns a boolean

s = solver()
s.add(ForAll(x, Implies(Mortal(x), True))) # all humans are mortal
s.add 