import string
from LogiComp.formula import Atom, And, Or
from LogiComp.functions import atoms

def satisfiablity_checking(formula):
  list_atoms = atoms(formula)
  interpretation = [] #conjunto vazio
  return sat(formula, list_atoms, interpretation)


def UniaoDeConjuntos(interpretacao, interpretacao2):
  intercecao = None
  return interpretacao + interpretacao2 - intercecao

def sat(formula, atoms, interpretation):
  if(len(atoms)==0):
    if(truth_value(formula, interpretation)):
      return interpretation
    else:
      False 
    
  atom = atoms.pop()
  interpretation1 = UniaoDeConjuntos(interpretation, {atom, True})
  interpretation2 = UniaoDeConjuntos(interpretation, {atom, False})
  result = sat(formula, atoms, interpretation1)
  if(result!= False):
    return result
  return sat(formula, atoms, interpretation2)
  

def truth_value():
  pass


print()
p = Atom('p')
q = Atom('q')
r = Atom('r')
s = Atom('s')


formula =  And(Or(r, r), r)


a = atoms(formula)
print(formula)
print(a)
print((formula.left))
