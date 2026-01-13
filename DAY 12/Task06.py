class geo:
    species="Human" #class variable
    def __init__(self,name): #instance variable
        self.nam=name

s=geo("A") #we can get different output using different object using instance varable
geo.species="Animal" #class variable data changes 

print("Species:",s.species)# output will be updated value of class variable
print("Name:",s.nam) #using instance variable


