def Flatten(lst):#define Flatten function
 for i in lst:  
   if type(i)==list: #checks if current number in a list or not, if is not in a list then else block run,otherwise
     yield from Flatten(i) #if current num in a list,flatten function() call again,for loop will run again,produce one by one value 

   else:
     yield i  #produce one value
l=Flatten([1, [2, [3, 4]]])
print(list(l))

