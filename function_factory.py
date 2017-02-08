def own_print(value):
    return value + " it's "

func = own_print('foo')

tmp = func

def func(value):
    return print(tmp + value)

func('bar')