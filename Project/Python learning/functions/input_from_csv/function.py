import csv
with open("example.csv", 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        lista = list(row)
dictionary = {i : 'True' for i in lista}
print(dictionary)
