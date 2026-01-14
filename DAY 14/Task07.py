lst = [1, 3, 5, 7, 9, 11,14]
target=3
low=0
high=len(lst)-1

while low<=high: #loop goes until low less than or equal to high
    mid=(low+high)//2 #mid value's index-3,2nd loop,low=0,high=2//2=1
    mid_value=lst[mid] #mid value-7,2nd loop,mid value-3

    if mid_value==target: #3==3
     print("Target value's index:",mid)
     break
    
    elif mid_value<target:
     low=mid+1 

    else:
     mid_value>target #target=3,loop comes here as 7>3
     high=mid-1 #3-1=2
