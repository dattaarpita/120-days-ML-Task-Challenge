def read_file(filename):
 with open(filename) as f:
  for line in f:
   yield line
fake_file=read_file("Data.txt")
print(next(fake_file))
print(next(fake_file))
print(next(fake_file))