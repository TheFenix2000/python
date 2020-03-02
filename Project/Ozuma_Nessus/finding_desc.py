from sys import argv
import xml.etree.ElementTree as ET

tree = ET.parse(argv[1])

for host in tree.findall('Report/ReportHost'):
    for item in host.findall('ReportItem'):
        desc = item.find('description').text
        print(desc)