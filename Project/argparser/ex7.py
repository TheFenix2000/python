#argumenty opcjonalne o przeciwnym znaczeniu użycie "add_mutually_exclusive_group()"

import argparse

parser = argparse.ArgumentParser(description="Calculate A to the power of X")
group = parser.add_mutually_exclusive_group()
group.add_argument("-q","--quiet",action="store_true",help="Handles it quiet")
group.add_argument("-v","--verbosity",action="store_true",help="Keeps it loud")
parser.add_argument("a",type=int,help="the base")
parser.add_argument("x",type=int,help="the index")
args = parser.parse_args()
answer = args.a**args.x

if args.quiet:
    print(answer)
elif args.verbosity:
    print("{} to the power of {} equals {}".format(args.a,args.x,answer))
else:
    print("{}^{} = {}".format(args.a,args.x,answer))