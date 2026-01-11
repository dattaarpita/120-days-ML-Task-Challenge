def wrapper(func):
    def before():
      print("Hello")
      print("How are you?")
      func()
    return before
# we can use this @wrapper, this automatically wraps the function to old()
def old_func():
    print("Arpita!")

new_func=wrapper(old_func)
new_func()
