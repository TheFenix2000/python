a = 47
b = 50
def f(): return 52
print('a={a}, b={b}, f={f}'.format(**locals()))
#użycie 'locals()' w format do przypisania wartości {a} odpowiada w słowniku locals key='a', etc.