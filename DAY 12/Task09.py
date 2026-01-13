class wallet1:
    def __init__(self,num):
        self.number=num
   

    def __add__(p,q): #these 2 parameters receive w1 and w2,add 2 objects
        return wallet1(p.number+q.number) #__init__ stores values, __add__ sum them

w1=wallet1(32)
w2=wallet1(54)
w3=w1+w2 #wallet1(86)
print(w3.number)#wallet1(86)
