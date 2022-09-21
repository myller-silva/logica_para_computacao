from formula import *
from functions import *

def number_of_binary_connectives(form):
  if(isinstance(form, Atom)):
    return 0
  if(isinstance(form, Not)):
    return number_of_binary_connectives(form.inner)
  if(isinstance(form, Or) or isinstance(form, And) or isinstance(form, Implies) ):
    return 1 + number_of_binary_connectives(form.left) + number_of_binary_connectives(form.right)


p = Atom('p') ; q = Atom('q')
r = Atom('r') ; s = Atom('s')
f = Or( And(p, And(Not(And(q, r)), Not(r)) ), s)

print(number_of_binary_connectives(Atom('p')))
print(number_of_binary_connectives(f))