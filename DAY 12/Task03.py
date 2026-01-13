class User:
    def __init__(self,name):
        self.name=name
    def __str__(self):#str uses for display 
        return "User:"+self.name
    def __repr__(self): #repr uses for debugging
        return"User:"+self.name
    
user=User("Arpita")
print(user) #if __str__ exists,print() will always print __str__ not __repr__
