#pozycyjne i opcjonalne argumenty w jednym algorytmie

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="Gives a square of a given number", type=int)
parser.add_argument("-o", "--optional", help="Increses detail of an output", action="store_true")
args = parser.parse_args()
answer = args.square**2 #zmienna przechowująca wynik z wpisanym argumentem przez użytkownika -> "square"
if args.optional:
    print("The square of {} equals {}".format(args.square, answer)) #uźycie "{}" w princie daje możliweość wypełneinia ich wartościami funkcji ".format()"
else:
    print(answer)