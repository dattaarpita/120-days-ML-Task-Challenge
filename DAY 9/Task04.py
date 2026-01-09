def g():
  for i in range(5):
    yield(i) 
gen=g()
#First loop will execute
for x in gen:
    print(x)
#Second loop will not execute
for x in gen:
    print(x)