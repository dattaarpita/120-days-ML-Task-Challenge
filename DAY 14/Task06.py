lst =[3, 1, 2, 3, 1,6,9,5,3,4,8]
s=set()
result=[]

for i in lst:
    if i not in s: #If i is in s, Python skips the if block and moves on to the next number in the loop
        result.append(i) #number added one by ine in result list
        s.add(i)#each unique number added here
print(result)

