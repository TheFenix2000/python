#różne wartości opcjonalnego argumentu poprzez zwielokrtnienie skróconej jego formy (-o,-oo)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,help="Gives a square of an number")
parser.add_argument("-o","--optional",action="count",help="Increases detail of an output",default=0) #wykorzystujemy action="count" | dodajemy "default=0 ponieważ przy braku otrzymujemy samą odp
args = parser.parse_args()
answer = args.square**2
if args.optional >= 2: # ">=" ponieważ jeżeli podamy więcej to otrzymujemy maksymalną wartość
    print("The square of {} equals {}".format(args.square,answer))
elif args.optional >= 1:
    print("{}^2 = {}".format(args.square,answer))
else:
    print(answer)