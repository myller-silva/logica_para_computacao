from formula import *
from functions import *

def is_term(form):
  if(isinstance(form, Atom)):
    return True
  if(isinstance(form, Not)):
    return True if(isinstance(form.inner, Atom)) else False
  if(isinstance(form, And)):
    if(not is_term(form.left)):
      return False
    if(not is_term(form.right)):
      return False
    return True
  return False