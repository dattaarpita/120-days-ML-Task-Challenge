a=[1,4,8,15,17]
b=[11,14,18,19,20]
merge=[]
i=j=0
while i<len(a) and j<len(b): # while loop stops if either i or j stops
    if a[i]<b[j]:
     merge.append(a[i])
     i=i+1
    else:
       merge.append(b[j])
       j=j+1
merge.extend(a[i:])#remaining value of a list added in merge list
merge.extend(b[j:]) #remaining value of b list added in merge list
print(merge)