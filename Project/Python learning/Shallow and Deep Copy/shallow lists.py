list1 = ['a', 'b', 'c', ['abc', 'def']]
list2 = list1

#listy wskazuja na to samo (shallow - płytki)
print(id(list1), 'list1')
print(id(list2), 'list2')

#czyli zmieniając element w liście 2nd zmieniamy 1st list
list2[0] = 'aa'

print(list1, 'list1')
print(list2, 'list2')

#to samo tyczy się sublist
print(id(list1[3]), 'sublist od list1')
print(id(list2[3]), 'sublist od list2')

#czyli zmiana elementu sublisty listy 2nd wpływa na listę 1st
list2[3][0] = 'ggg'

print(list1[3], 'sublist of list1')
print(list2[3], 'sublist of list2')