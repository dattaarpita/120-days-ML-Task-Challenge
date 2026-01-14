from itertools import groupby
from operator import itemgetter
lst_dict=[{"category":"Student","Name":"Arpita"},
          {"category":"Teacher","Name":"B"},
          {"category":"Student","Name":"Rachel"},
          {"category":"Teacher","Name":"B"}]

sort=sorted(lst_dict,key=itemgetter("category"))#list of dictionary sorted based on "category" key.
for category,name in groupby(sort,key=itemgetter("category")):#"groupby" keyword groups dictionary based on sort dictionary's key, similiar keys's data will be grouped together,groupby() returns pairs (2 values),key,group.
    print(category,list(name))
