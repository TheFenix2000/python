from copy import deepcopy

list1 = ['a', 'b', ['aa', 'bb']]
list2 = deepcopy(list1)
#ta sama zawartoś ale inne id czyli kopiujemy zawartość
print(id(list1), ' - list1', '\n', list1, '\n')
print(id(list2), ' - list2', '\n', list2, '\n')

#listy wkazuja na ten sam element 0th
print(id(list1[0]), 'Element 0th of list1')
print(id(list2[0]), 'Element 0th of list2\n')

#ale element 2nd już jest w innych miejscach w pamięci czyli wstakuja na osobne sublisty
print(id(list1[2]), 'Element 2nd of list1')
print(id(list2[2]), 'Element 2nd of list2')

#zmiany nie kolidują ze sobą
list1[2][1] = 'dd'
list2[0] = 'd'

print(list1)
print(list2)

