lst= ["100px","20px","3px"]
result=sorted(lst,key=lambda x:int(x[:-2])) #key keyword used here for comparison not changing anything
print(result)