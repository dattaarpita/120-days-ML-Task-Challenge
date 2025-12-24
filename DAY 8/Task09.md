Code: Measure the time to create a dict from a list vs searching it

Explantion:Here a list is created of 10 mllion numbers. Then list is converted to a dictionary. For time measurement ,time module is imported. Before starting
to create a dictionary time.time() called.Then after creation of dict,time.time() it is called again. Then found a time that is needed to create
dictionary.It takes more time.
Then when searching the element in dictionary,time.time()is called again.But it takes less time than before.Because while searching it uses hash value
and direct jumps bucket_index and found that number. Its more fast.

