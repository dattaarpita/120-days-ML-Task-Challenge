def gen():
    val=yield #yield pauses execution, and .send() resumes it and place value into yield
    print(val)

g=gen()
next(g)
g.send("hello")
