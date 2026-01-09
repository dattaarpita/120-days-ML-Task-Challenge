import sys
lst = [x for x in range(1000000)]
print("List:",sys.getsizeof(lst)) 
gen = (x for x in range(1000000))
print("Generator:",sys.getsizeof(gen)) 

#in list,all numbers stored in memory.in gen, number dont store .only logic stores.loop variable stores ,when next()calls,reference/pointer returns that value but dont store