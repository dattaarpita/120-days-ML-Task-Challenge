def a():
    for i in range(5):
        yield i
def b():
 lst=["a","b","c"]
 yield lst
def generator():
    yield from a()
    yield from b()
gen= generator()
for x in gen:
    print(x)
