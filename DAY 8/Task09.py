import time
mylist=list(range(10000000))
start=time.time()
mydict={i:"Ditionary" for i in mylist}
end=time.time()
time_allocated=end-start
print("Time needed to create a dictionary:",time_allocated)
start=time.time()
if 2000 in mydict:
 print("Element found")
end=time.time()
total_time=end-start
print("Time needed to find an element from a dictionary:",total_time)
