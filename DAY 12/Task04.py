class User:
    def __init__(self,password):
        self.__password=password #name mangling it will store as _User__password
    def private_value(self,current_value):
        return self.__password==current_value 
    
user=User(12)
print(user._User__password) #encapsulation happens because __password creates _User__password internally ,it can't be accessed by public
print(user.private_value(12)) #this is public accessable, used to see result,private function is hidden from this