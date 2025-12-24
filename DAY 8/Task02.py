#Linear searchinh through set is more faster than list
lst=list(range(10000000))
set=set(lst)
target=-5
if target in set:
    print("Number is found")
else:
    print("Number is not found")