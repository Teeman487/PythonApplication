from functools import partial
#functools.partial allows you to create a new function with some of the arguments of an existing function pre filled

def add(a, b):
    return a+b
add_five=partial(add,5)
print(add_five(3))