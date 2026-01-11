def repeat(times=3): #decorator factory returns decorator
 def decorator(func): #actual decorator takws original func
     def wrraper(): #arg uses here
        for i in range(times):
         func()       
     return wrraper
 return decorator
@repeat(times=3)
def original_func():
    print("hello")
original_func()