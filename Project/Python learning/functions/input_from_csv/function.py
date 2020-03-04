import csv

default_excluded_id_file = "excluded_ids.csv"
class nessus:
    global dictionary
    def __init__(self, filename=None):
        self.filename = filename
    def __get_excluded_ids_from_file(self, filename):
        with open(filename, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                lista = list(row)
        dictionary = {i: 'True' for i in lista}
        print(dictionary)
    def __get_excluded(self):
        d = default_excluded_id_file
        with open(d, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                lista = list(row)
        dictionary = {i: 'True' for i in lista}
        print(dictionary)
    def show(self):
        self.__get_excluded_ids_from_file('example.csv')
        self.__get_excluded()


with open(default_excluded_id_file, 'r') as file:
    csv_file = csv.reader(file)
    for row in csv_file:
        {}