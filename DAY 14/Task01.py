lst=[1,2,3,5]
target =5
seen={}

for i,j in enumerate (lst):#i gives index,j gives value
 needed = target - j #needed variable stores subtraction of target & current index's value

 if needed in seen: 
  print("Indexes:",[seen[needed],i])
  print("Sum",lst[seen[needed]]+lst[i])#seen[needed] gives index number not value,i also index no.
  break
 
 else:
  seen[j]=i #in seen dictionary, seen[j]->value represents as key,i->index acts as value.{1:0,2:1,3:2}

