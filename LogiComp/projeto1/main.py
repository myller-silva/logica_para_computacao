def satisfiablity_checking(formula):
  list_atoms = atoms(formula)
  interpretation = [] #conjunto vazio
  return sat(formula, list_atoms, interpretation)

def atoms():
  pass


def sat(formula, atoms, interpretation):
  if(len(atoms)==0):
    if(truth_value(formula, interpretation)):
      return interpretation
    else:
      False 
    
  atom = atoms.pop()
  interpretation1 = interpretation U {atom, True}
  interpretation2 = interpretation U {atom, False}
  result = sat(formula, atoms, interpretation1)
  if(result!= False){
    return result
  }
  return sat(formula, atoms, interpretation2)
  

def truth_value():
  pass