import time
mylist=list(range(10000000))
#here slice size(k)=5000
start=time.time()
data=mylist[0:5000]
end=time.time()
time_needed=end-start
print("Time:",time_needed)