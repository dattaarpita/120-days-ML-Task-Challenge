import json
dict={"Name":"Arpita",
      1:"Roll"}

with open("dict.json","w") as f:
    json.dump(dict,f) #here in dict int 1 must be string "1" & dict.json file created and write dictionary data into json format in dict.json file.