#!/usr/bin/python3

#Tabla Multiplicar

Numbers = list(range(1,11))

for number1 in Numbers:
    for number2 in Numbers:
        mult = number1 * number2
        print(number1, "por", number2, "=", mult)
