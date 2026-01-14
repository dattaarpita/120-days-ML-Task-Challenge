lst=list(range(1,101))
lst.remove(6)

actual_sum= 100*(100+1)//2
missing_sum=sum(lst)
difference=actual_sum-missing_sum

print("Missing value:",difference)