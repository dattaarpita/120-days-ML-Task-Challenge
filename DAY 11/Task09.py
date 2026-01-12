from functools import partial
def power (base, exp):
    return base **exp
#partial func frezee exp=2
square=partial(power,exp=2)
print(square(3))