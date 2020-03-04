import csv

DEFAULT_EXCLUDED_FILENAME = "excluded_ids.csv"

class ExcludedLoader:
    def __init__(self, filename=None):
        if filename is not None:
            self._filename = filename
        else:
            self._filename = DEFAULT_EXCLUDED_FILENAME

    def get_excluded(self):
        return self._get_excluded_ids_from_file(self._filename)

    def _get_excluded_ids_from_file(self, filename):
        with open(filename, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                dictionary = {i: True for i in row}
                return dictionary


class DummyExcludedLoader:
    def get_excluded(self):
        return {'123' : True, '456' : True}

class Nessus:
    def __init__(self, zosia):
        self._exluded_loader = zosia

    def process(self):
        excluded = self._exluded_loader.get_excluded()
        print(excluded)
    
#ld = DummyExcludedLoader()

ld = ExcludedLoader()

n = Nessus(ld)
n.process()
