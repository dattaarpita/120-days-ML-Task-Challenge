def wrapper(func):
    def inner_wrap_function(*args,**kwargs):
        print("Add something")
        return func(*args,**kwargs)
    return inner_wrap_function
@wrapper
def old_func(a,b):
    return a+b

print(old_func(2,3))
