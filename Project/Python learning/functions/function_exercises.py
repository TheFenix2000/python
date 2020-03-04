def Hello(name="everybody"):  #everybody to deafult value of name
    """Greets a person"""
    print('Hello there: ' + name + '!')
Hello()
Hello('Peter')
print('The docstring od function Hello: ' + Hello.__doc__)  #__doc__ to taki 'tytuł' funkcji

#parametr
def Sum_sub(a, b, c=0, d=0):
    return a - b + c - d
print('\n', Sum_sub(12,4))
print(Sum_sub(12,4,d=10))

def Fibonacci_intervall(x):
    """returns te largest fibonacci number smaller than x
    and lowest fibonacci number higher ten s"""
    if x < 0:
        return -1
    (old, new, lub) = (0, 1, 0)
    while True:
        if new < x:
            lub = new
            (old, new) = (new, old + new)
        else:
            return (lub, new)
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = Fibonacci_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))