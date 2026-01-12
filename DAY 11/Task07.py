#using for loop
num=[]
for x in range(10):
    num.append(x)
print("Using for loop:",num)
#using map+lambda
result=list(map(lambda x: x,range(10))) #map takes each value for lambda,then operation happens
print("Using map:",result)
