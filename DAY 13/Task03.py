with open("a.png","rb") as f: #images  read as binary mode,return as bytes
    data=f.read()
print(type(data))