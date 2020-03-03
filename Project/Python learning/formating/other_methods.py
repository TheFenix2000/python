#środkowanie w podanej 'szerokości'
s = "Python"
print(s.center(10, '*'))

#justowanie do lewej i prawej
print(s.ljust(10, ';'))
print(s.rjust(10, '~'))

#wypełnianie 0 od lewej = rjust
number = "1221"
print(number.zfill(10))
print(number.rjust(10, '0'))