def wrapper(func):
  def inner_func(*args,**kwargs):
     func(*args,**kwargs)
  return inner_func

@wrapper
def old_func(a,b):
    return a+b
print("Result:",old_func(2,1))