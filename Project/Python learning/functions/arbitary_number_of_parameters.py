def f(**kwargs):
    print(kwargs)
f(de='German', en='English', fr='French')

def f1(a, b, y, x):
    print(a, b, y, x)
d = {'a': 'Hello', 'b': 'there', 'x': 'Kenobi', 'y': 'General'}
f1(**d)