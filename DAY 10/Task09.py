def bold(fun):
    def inner():
      print("Bold") 
      return fun() # goes to wrapper function
    return inner

def italic(func):
    def wrapper():
      result=func()#original function
      print("Italic:",result) 
      return result
    return wrapper

@bold #outer decorator will run first
@italic #inner decorator will run secondly,wraps the original func
def original_func():
  return "hello"
original_func()
