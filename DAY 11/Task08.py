nums = [1,-2,3, 4]
result=any(x<0 for x in nums) #any gets true if one value are true 
print(result)

num=[1,-2,3,4]
result=all(x>0 for x in num) #all gets false if one value doesn't satify cobdition
print(result)