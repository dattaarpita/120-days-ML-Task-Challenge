def linear_search(lst,target):
    for i in range(len(lst)):
        if lst[i]==target:
            return "Number Found"
    else:
        return "Number not Found"
array=list(range(10000000))
target=-5
variable=linear_search(array,target)
print(variable)

