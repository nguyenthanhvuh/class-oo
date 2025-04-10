# Z3 

import z3
from z3 import *    # import all Z3 functions

# some good examples here https://hanielbarbosa.com/papers/fm2024.pdf


# Declare symbolic variables
x = Int('x')
y = Int('y')
z = Int('z')

# ¬a ∧ b < 5 ∧ ¬a ∧ c 

f = z3.And(x + y == 150, x * z == 2025) 

g = z3.And(y == -1875, x == 2025, z == 1)

s = Solver()
s.add(f)
s.add(z3.Not(g)) 

print(s)
if (s.check() == z3.sat):
    print(s.model())
else:
    print("unsat")





# # Create a solver
# s = Solver()

# # Add path constraints based on the nested conditionals
# s.add(x + y == 150)
# s.add(x * z == 2025)

# if s.check() == sat:
#     print(s.model())
# else:
#     print('unsat')