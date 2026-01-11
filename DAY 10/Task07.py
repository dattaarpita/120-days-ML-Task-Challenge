def cache(func):
    dict={}
    def inner(n):
        if n in dict:
            print(f"The number {n} from dictionary")
            return dict[n]
        store=func(n)
        dict[n]=store
        return store
    return inner

@cache
def exp_func(n):
    if n<=1:
       return n
    return exp_func(n-1)+exp_func(n-2)
print("Result:",exp_func(4))




