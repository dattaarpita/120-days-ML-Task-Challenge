class User:
    def __init__(self,name):
        self.nam=name

class Admin(User):
    def __init__(self,name,age):
        super().__init__(name) #when both child and parent class have __init__(),super().__init__() must use in child's class for executing User classes __init__()function
        self.age=age

a=Admin("ARPITA",25)

print(a.nam)
print(a.age)
