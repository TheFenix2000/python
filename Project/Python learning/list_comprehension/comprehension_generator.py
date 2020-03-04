#generator has round brackets instead of square-ones

def f(input_range):
    x = (x ** 2 for x in range(input_range))
    return print(list(x))
f(20)