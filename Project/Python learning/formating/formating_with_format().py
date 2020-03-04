print('First argument: {0}, second argument: {1}'.format(1223,3321))

print('First argument: {}, second argument: {}'.format(1223,3321))

#zmiana kolejności
print('Second argument: {1}, first argument: {0}'.format(1223,3321))

print('Second argument: {1:5f}, first argument: {0:7d}'.format(1223,3321.123))

#możliwość użyciea tego samego argumenty kilka razy
print('first argument: {0:2.2f}, same argument: {0:2.3f}'.format(47.2315))

#użycie key=
print('First argument: {a:2.2f}, second argument: {b:5d}'.format(a=23.2376, b=276))

#wyrównania do lewej i prawej
print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

#sygnalizacja 'szerokości' argumentu
x = 376
print('The value of x is: {:06d}'.format(x))
x = -376
print('The value of x is: {:06d}'.format(x))

#przecinek jako oddzieenie tysięcy
x = 122332432
print('The value of x is: {:,}'.format(x))

#środkowanie
x = 'Hi there'
print('{:^20s}{}'.format(x, 12121))