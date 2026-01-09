def gen():
    yield 1
    yield 2
    yield 3
for x in gen():
  print(x)

#gen() function includes: yield and next().when next() calls then value of 1st yield executes. After execution yield pauses until next() calls again.
#Because gen produce only one value at a time, and then pause.