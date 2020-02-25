#!/usr/bin/python

from sys import argv
import xml.etree.ElementTree as ET

tree = ET.parse(argv[1])

plugin, risk, description = "Plugin,", "Risk,", "Description"
print(plugin + risk + description)

full_list = []
for host in tree.findall('Report/ReportHost'):
  des = host.findall('[@description]').text
  print(des)
  for item in host.findall('ReportItem'):
    des = item
    risk_factor = item.find('risk_factor').text
    pluginID = item.get('pluginID')
    pluginName = item.get('pluginName')

    order = {
      "Critical":0,
      "High":1,
      "Medium":2,
      "Low":3,
      "None":4
    }

    four = (order[risk_factor], pluginID, risk_factor, pluginName)
    full_list.append(four)
    full_list.sort()

excluded_IDs = [19506, 10386, 10662, 10287]
result_list = []
for i in full_list:
  if i[1] not in str(excluded_IDs):
    result_list.append(i)
numb_of_rows = 0
for x in result_list:
  if x[0] < 4:
    numb_of_rows+=1