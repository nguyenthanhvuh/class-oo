from z3 import *

# Define the variables
i = Int('i')
N = Int('N')

# Define the expression
# (i = 0 ∧ N > 0) ⇒ (i ≥ N ⇒ i = N)
expression = Implies(And(i <= N, i < N), i+ 1 <= N)

prove(expression)