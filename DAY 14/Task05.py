for i in range(1,101):
  pass
  if i%15==0: #this condition written first because if it was written at last, this block wont run, first block would run always, cause that would satisfy first and print result.
    print("FizzBuzz")
  elif i%5==0:
    print("Buzz")
  elif i%3==0:
    print("Fizz")
  else:
    print(i)
