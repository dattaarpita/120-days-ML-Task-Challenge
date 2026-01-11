from functools import wraps
def decorator(func):
    @wraps (func)
    def wrapper():
        func()
    return wrapper
@decorator
def original_func():
    print("Original function!!")  
    
original_func()
print(original_func.__name__)
