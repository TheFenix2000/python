#funkcja z opcjonalnym argumentem

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--optional", help="You don't have to write me down", action="store_true")#jeżeli podana jest ta opcja będzie output
args = parser.parse_args()
if args.optional:
    print("How kind of you :)")
#możemy równieź nadać krótką formę naszemu argumentowi