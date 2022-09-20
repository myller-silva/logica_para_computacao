from formula import *
from functions import *

def number_of_connectives(A):
  if(isinstance(A, Atom)):
    return 1;
  if(isinstance(A, Not)):
    return 1 + number_of_connectives(A.inner);
  if(isinstance(A, Or) or isinstance(A, And) or isinstance(A, Implies)):
    return 1 + number_of_connectives(A.left) + number_of_connectives(A.right);


p = Atom('p');
q = Atom('q');
r = Atom('r');

fol = Implies(p, q)
print(fol)
print(f'numero de conectivos: {number_of_connectives(fol)}')



