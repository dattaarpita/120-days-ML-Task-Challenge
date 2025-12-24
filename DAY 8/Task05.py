my_list=""
for i in range(10000):
    my_list+="a"
    print(my_list)

#using .join()
my_list=[]
for i in range(10000):
    my_list.append("a")
new_list=''.join(my_list)
print(new_list)