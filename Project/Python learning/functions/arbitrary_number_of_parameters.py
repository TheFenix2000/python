#średnia arytmetyczna z podanych wartości
def Arthmetical_mean(first, *values):
    """This function calculates the arthmetical mean of a non-empty arbitrary number of numerical values"""
    return (first + sum(values)) / (1 + len(values))

print(Arthmetical_mean(10, 20, 30))
print('{:5.2f}'.format(Arthmetical_mean(20.43, 223.987, 2331.5554)))
print(Arthmetical_mean(45))

#średnia aryt. z listy
x = [12, 133, 32, 44, 10, 3232, 456, 34, 1, 121, 3234, 99, 90, 897]
print('{:6.2f}'.format(Arthmetical_mean(*x)))

#zmiana listy tupli na słownik
my_list = [('a', 12), ('b', 20), ('c', 30), ('d', 40)]
second_list = list(zip(*my_list))
print(second_list)
dictionary = dict(my_list)
print(dictionary)
