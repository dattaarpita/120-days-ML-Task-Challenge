class User:
 name="Arpita"
 age=25

class Admin(User): #Admin child class,User parent class
  def delete_db(self):
    return("Delete DB")
   
c=Admin()
print(c.name) #child class's object c, inherits parent class's attribute
print(c.delete_db())

