my_list=[1,2,3,4,5]
print("List",my_list)
#pop() remove last element from list
my_list.pop() 
print("After removing last element,List:",my_list)

my_list1=[1,2,3,4,5]
#pop(0) remove very first element from list,it effects on performance
my_list1.pop(0) 
print("After removing first element,List:",my_list1)

#deque uses for fast operation
from collections import deque
de=deque([1,2,3,4,5])
de.pop()
de.popleft()
print("List using deque:",de)

