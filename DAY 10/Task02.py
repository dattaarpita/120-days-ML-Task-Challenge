def wrapper(wrap_func):
    def inside_func():
        print("Hi!!")
        print("This is inside function")
        wrap_func()
    return inside_func
@wrapper
def old_function():
    print("This is outside function")
old_function()
