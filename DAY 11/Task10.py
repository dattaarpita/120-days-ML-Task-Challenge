t=(1,2,3)
#modify_tuple=tuple(map(lambda x:t[0]=10,t))#in lambda function assignment impossible,tuple can't be modified,instead better to create new tuple
#print(modify_tuple)
new_tuple=tuple(map(lambda x:x*2,t))#creates new tuple,not modifying previous tuple
print(new_tuple)