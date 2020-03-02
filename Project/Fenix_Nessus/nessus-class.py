#!/usr/bin/python

from sys import argv
import xml.etree.ElementTree as ET

tree = ET.parse(argv[1])
full_list = []

class Nessus:

  def ExcludeID(self):
    """User adds excluded IDs"""
    how_many_numbers = int(input("Number of ignored IDs to add: "))
    if not how_many_numbers == 0:
      with open('excludedIDs.csv', 'a') as write_into:  #append ids to given file
        for number in range(0, how_many_numbers):
          number = int(input('Ignored ID: '))
          write_into.write(',' + str(number))  #IDs write to file

  def Find_Items(self):
    """Searches for elements in source file"""
    for host in tree.findall('Report/ReportHost'):
      for item in host.findall('ReportItem'):  #defined elements
        risk_factor = item.find('risk_factor').text
        pluginID = item.get('pluginID')
        pluginName = item.get('pluginName')
        description = item.find('description').text
        order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3, "None": 4}

        def List_append():
          """Open > append elements (without excluded IDs)"""
          with open('excludedIDs.csv', 'r') as read_from:
            readed = read_from.read()
            if pluginID not in readed:
              five = (order[risk_factor], pluginID, risk_factor, pluginName, description)
              full_list.append(five)
              full_list.sort()
        List_append()

    print(full_list)

def Main():
  """Main function"""
  nessus = Nessus()
  nessus.ExcludeID()
  nessus.Find_Items()


if __name__ == '__main__':
  Main()