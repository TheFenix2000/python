from prettytable import PrettyTable as PT
from prettytable import from_csv

order = {
    "Low":0,
    "Medium":1,
    "None":2
}
file_path = "nessus_result.csv"
with open(file_path, "r") as csv_fie:
    x = from_csv(csv_fie)
x.field_names = ['IP','RISC FACTOR','PORT/PROTOCOL','PLUGIN ID','DESCRIPTION']
value =  x.get_string(fields = ["PLUGIN ID", "RISC FACTOR", "DESCRIPTION"])
