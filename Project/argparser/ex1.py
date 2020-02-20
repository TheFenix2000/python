#przykładowa funkcja z wymaganym argumentem

import argparse

parser = argparse.ArgumentParser()#działanie kodu
parser.add_argument("square", type=int ,help="gives a square of a given number")#specyfikacja dodanego argumentu
args = parser.parse_args()#wartość przechwująca nasze wpisane argumenty
print(args.square**2)#wyświetlanei funkcji