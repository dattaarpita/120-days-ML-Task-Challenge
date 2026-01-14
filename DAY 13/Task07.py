with open("Largefile.txt","w") as f:
    for i in range(1000000):
        f.write(f"{i}\n") #here f.write() didn't write line one by one.instead it sends chunks of data(here lines) to disk.Chunk of data stored in ram,when chunk size is full,it goes to disk.
    