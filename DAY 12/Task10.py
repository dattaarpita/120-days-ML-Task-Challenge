class User:
    def __init__(self,num):
        self.no=num
    def __eq__(a,b):#by default u1 and u2 are different object so they are not equal.memory address different.when __eq__use,it checks value, equal or not
        return a.no==b.no
    
u1=User(1)
u2=User(1)
print(u1==u2) 
