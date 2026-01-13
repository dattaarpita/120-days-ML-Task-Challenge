from datetime import date
class User:
    def __init__(self,birth_year):
        self.birth_y=birth_year

    @property  #this keyword works as encapsulation, age is not normal function, when calling it looks like variable but it is function actually
    def age(self):
     return date.today().year-self.birth_y
    
user=User(2001)
print(user.age) 