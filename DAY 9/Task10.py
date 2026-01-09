def avg_gen():
    total=0
    count=0
    while True :
     number=yield total/count if count else "No number is given yet"
     total=total+number
     count= count+1
    
g=avg_gen()
print(next(g))
print("First average:",g.send(5))
print("Second average:",g.send(10))
print("Third average:",g.send(15))