#różne wartości opcjonalnego argumentu (choices=[])

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-o", "--optional", type=int,
                    help="increase output verbosity", choices=[0,1,2])
args = parser.parse_args()
answer = args.square**2
if args.optional == 2:
    print ("the square of {} equals {}".format(args.square, answer))
elif args.optional == 1:
    print ("{}^2 == {}".format(args.square, answer))
else:
    print (answer)