def fib_num():
    a,b=0,1
    while True:
     yield a
     a,b=b,a+b   
gen=fib_num()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
