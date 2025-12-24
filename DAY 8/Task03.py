#Taking user input
user_input=input("Enter some numbers:")
list_append=[int(x) for x in user_input.split(',')]
print("List Before apppend:",list_append)
#Taking a number  to append
y=int(input("Enter a number to append:"))
list_append.append(y)
#Print whole list after appending a number
print("List after append:",list_append)

#Using insert()
user_input=input("Enter some numbers:")
list_insert=[int(x) for x in user_input.split(',')]
print("List Before insert:",list_insert)
z=int(input("Enter a number to insert:"))
index_no=int(input("Enter an index number you want to insert a number:"))
list_insert.insert(index_no,z)
print("List after insert:",list_insert)