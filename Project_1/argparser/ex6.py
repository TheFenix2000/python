#potęgowanie jako funkcja z opcjonalnym parametrem szczegółowości

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("a", type=int, help="podstawa")
parser.add_argument("x", type=int, help="wykładnik")
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()
answer = args.a**args.x
if args.verbosity >= 2:
    print ("{} to the power {} equals {}".format(args.a, args.x, answer))
elif args.verbosity >= 1:
    print ("{}^{} == {}".format(args.a, args.x, answer))
else:
    print (answer)