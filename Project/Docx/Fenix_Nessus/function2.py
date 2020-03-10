import csv
from sys import argv
import xml.etree.ElementTree as ET

DEFAULT_EXCLUDED_FILENAME = "excludedIDs.csv"
tree = ET.parse(argv[1])
full_list = []


class _Nessus:
    def find_items(self):
        """Searches for elements in source file"""
        for host in tree.findall('Report/ReportHost'):
            for item in host.findall('ReportItem'):  # defined elements
                risk_factor = item.find('risk_factor').text
                pluginID = item.get('pluginID')
                pluginName = item.get('pluginName')
                description = item.find('description').text
                order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "None": 4}
                five = (order[risk_factor], pluginID, risk_factor, pluginName, description)
                full_list.append(five)
                full_list.sort()
                return print(full_list)
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

class Nessus:
    def __init__(self, excluded_loader):
        self._excluded_loader = excluded_loader

    def process(self):
        excluded = self._excluded_loader.get_excluded()

if __name__ == "__main__":
    ld = ExcludedLoader()
    n1 = _Nessus()
    n1.find_items()
    n = Nessus(ld)
    n.process()
