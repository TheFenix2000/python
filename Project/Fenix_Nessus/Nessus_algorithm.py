#!/usr/bin/python

from sys import argv
import xml.etree.ElementTree as ET
import csv

DEFAULT_EXCLUDED_FILENAME = "excludedIDs.csv"

class NessusFile:
  def __init__(self, tree):
    self._tree = tree

  def find_items(self):
    full_list = []

    for host in self._tree.findall('Report/ReportHost'):
      for item in host.findall('ReportItem'):
        risk_factor = item.find('risk_factor').text
        pluginID = item.get('pluginID')
        pluginName = item.get('pluginName')
        description = item.find('description').text
        order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "None": 4}

        five = (order[risk_factor], pluginID, risk_factor, pluginName, description)
        full_list.append(five)

    full_list.sort()
    return full_list

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

class NessusProcess:
  def __init__(self, excluded_loader):
    self._excluded_loader = excluded_loader

  def process(self, full_list):
    excluded = self._excluded_loader.get_excluded()
    result_list = [ x for x in full_list if x[1] not in excluded ]
    print(result_list)

def main(nessus_filename):
  """Main function"""
  tree = ET.parse(nessus_filename)

  nessus = NessusFile(tree)
  full_list = nessus.find_items()

  ld = ExcludedLoader()
  n = NessusProcess(ld)
  n.process(full_list)


if __name__ == '__main__':
  nessus_filename = argv[1]
  main(nessus_filename)