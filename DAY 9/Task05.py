def g():
    i=0
    for i in range(5):
     yield i
    
gen=g()
try:
    while True: 
       print(next(gen))     

except StopIteration:
    print("Generator runs out of items")