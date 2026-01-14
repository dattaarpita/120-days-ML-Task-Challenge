import pickle #pickle means binary format
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
u=User("Arpita",25)
with open("User.pkl","wb") as f: 
    pickle.dump(u,f) #with open() created User.pkl file.pickle.dump() takes object and convert data into binary format and stored in User.pkl