#!/usr/bin/env python3
import z3

# Variables
a, b, c = z3.Ints('a b c')

# Constraint: a^2 + b^2 = c^2
pythagorean_constraint = z3.ForAll([a, b, c], z3.Implies(And(a > 0, b > 0, c > 0), z3.Or(a**2 + b**2 != c**2, a == 3, b == 4, c == 5)))

# Solve
solver = z3.Solver()
solver.add(pythagorean_constraint)
print("Pythagorean Triples with a^2 + b^2 = c^2 are satisfiable:", solver.check())
