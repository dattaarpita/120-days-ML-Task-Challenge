Convert that list to a set. Check for -5 again.
Code:
#Linear searching through set is more faster than list
lst=list(range(10000000))
set=set(lst)
target=-5
if target in set:
    print("Number is found")
else:
    print("Number is not found")

Explanation:
In this task list is created of 10 million numbers . Then converted to set. It is more faster than list. Because in list, linear searching,
it checks all the numbers one by one.But when list is converted to set, when we are going to serach a number, python immediately finds its hash
value.Then jump into its memory location instead of checking one by one. It occurs instant and faster than list.


