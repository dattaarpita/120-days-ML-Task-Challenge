import time
def timer(func):
  def inner_func(*args,**kwargs):
     start=time.time()
     sum=func(*args,**kwargs)
     end=time.time()
     print("Execution time:",end-start)
     return sum
  return inner_func
 
@timer
def old_func(a,b):
    return a+b
print("Result:",old_func(2,1))
