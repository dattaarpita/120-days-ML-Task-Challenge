import csv
dict=[]

with open("Data.csv","r") as f:                    
    c=csv.DictReader(f) #csv.DictReader() reads csv file and converts each row to dictionary, column headers become keys and each row will count as values
    for i in c:
        dict.append(i)
        print(i)