import definition
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("catalog_name", help="Name of the catalog")

args = parser.parse_args()
definition.convert(args.catalog_name)

