from formula import *
from functions import *

def number_of_atoms(form):
  if(isinstance(form, Atom)):
    return 1
  if(isinstance(form, Not)):
    return number_of_atoms(form.inner)
  if(isinstance(form, Or) or isinstance(form, And) or isinstance(form, Implies)):
    return number_of_atoms(form.left) + number_of_atoms(form.right)

p = Atom('p') ; q = Atom('q')
r = Atom('r') ; s = Atom('s')
f = Or( And(p, And(Not(And(q, r)), Not(r)) ), s)

print(number_of_atoms(p))
print(number_of_atoms(Not(Implies(p, q))))
print(number_of_atoms(f)) 
print(number_of_atoms(Or( And(p, Not(Implies(p, Not(q)))), Not(q) ) )) #((p ∧ ¬(p → ¬q)) ∨ ¬q) = 4


