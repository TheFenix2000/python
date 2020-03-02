tup = [('123', "Hello"), ('19506', 'there'), ('1111', 'Kenobi')]

how_many_numbers = int(input("Number of ignored IDs to add: "))
if not how_many_numbers == 0:
  with open('excludedIDs.csv', 'a') as write_into:
    for number in range(0, how_many_numbers):
      number = int(input('Ignored ID: '))
      write_into.write(',' + str(number))

for item in tup:
    first = item[0]
    second = item[1]
    with open('excludedIDs.csv', 'r') as file:
        readed = file.read()
    if first not in readed:
        print(second)