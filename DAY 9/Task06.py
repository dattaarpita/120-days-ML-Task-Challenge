#squares numbers, the other filters evens
try:
  def square_num(n):
   i=0
   for i in range(n):
      yield i**2
      

  def filter_evens(j):
   for x in j:
     if x%2==0:
        yield x
   
  square=square_num(10)
  evenn=filter_evens(square)

  print("1st even number:",next(evenn))
  print("2nd even number:",next(evenn))
  print("3rd even number:",next(evenn))
  print("4th even number:",next(evenn))
  print("5th even number:",next(evenn))
  print("6th even number:",next(evenn))
  print("7th even number:",next(evenn))

except StopIteration:
  print("Stop!!")



