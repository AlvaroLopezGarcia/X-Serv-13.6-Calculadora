#!/usr/bin/python3

#Álvaro López García

import sys

try:
    operador = sys.argv[1]
    num1 = float(sys.argv[2])
    num2 = float(sys.argv[3])
except IndexError:
    print("usage : [operador][num1][num2]")
except ValueError:
    print("El argumento 2 y 3 tienen que ser tipos numericos")

try:
    if operador == "suma":
        print(num1 + num2)
    elif operador == "resta":
        print(num1 - num2)
    elif operador == "multiplicacion":
        print(num1 * num2)
    elif operador == "division":
        try:
            print(num1 / num2)
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
    else:
        print("Tienes que usar un operador matematico como: suma, resta, multiplicacion o division")
except NameError:
    print("No han sido definidos todos los argumentos")
        
