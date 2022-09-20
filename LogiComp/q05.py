from typing import OrderedDict
from formula import *
from functions import *


def atoms(A):
  if(isinstance(A, Atom)):
    return [A.name];
  if(isinstance(A, Not)):
    return atoms(A.inner);
  if(isinstance(A, Or) or isinstance(A, And) or isinstance(A, Implies) ):    
    return list(OrderedDict.fromkeys(atoms(A.left) + atoms(A.right)));


p = Atom('p'); q = Atom('q'); r = Atom('r');
j = Atom('j'); l = Atom('l'); m = Atom('m');

f1 = Or(And(p, Not(Implies(p, Not(q)))), Not(q))

print(f1)
print( atoms(f1), end='\n\n' )
f2 = Not(Implies(Implies(Not(r), p), Not(q)))
print(f2)
print( atoms(f2), end='\n\n' )
f3 = Implies( And(f1, Implies(Not(f2), r)), Or(Not(q), m) )
print(f3)
print( atoms(f3), end='\n\n' )
