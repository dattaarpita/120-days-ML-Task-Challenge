import time
class Timer:
    def __enter__(s):
        s.time=time.time()
    def __exit__(s,exc_type, exc_value, traceback): #__exit__functions built in arguments exc_type, exc_value, traceback
        print("Total time:", time.time()-s.time)

with Timer(): #Timer()creates a object s,it will send back to class Timer,there enter function will run, start time will calculate.then block inside with Timer() will execute, then exit function run.
    time.sleep(10)