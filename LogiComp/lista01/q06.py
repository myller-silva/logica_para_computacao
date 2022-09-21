from formula import *
from functions import *


def is_negation_normal_form(formula):
  if(isinstance(formula, Atom)):
    return True
  if(isinstance(formula, Not)):
    return True if (isinstance(formula.inner, Atom)) else False
  if(isinstance(formula, Or) or isinstance(formula, And)):
    if(not isinstance(formula.left, Atom)):
      return is_negation_normal_form(formula.left)
    if(not isinstance(formula.right, Atom)):
      return is_negation_normal_form(formula.right)
    return True
  return False



p = Atom('p') ; q = Atom('q')
r = Atom('r') ; s = Atom('s')
f = Or( And(p, And(Not(And(q, r)), Not(r)) ), s)

print(f)
print(is_negation_normal_form(f))
print(is_negation_normal_form(p))
print(is_negation_normal_form(Not(p)))
print(is_negation_normal_form(Not(And(p, r))))
print(is_negation_normal_form(Not(Or(p, r))))

print(is_negation_normal_form( Or( And(p, And(And(Not(q), r), Not(r))), s)))


print(is_negation_normal_form( Or(p, q) ))