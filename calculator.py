#!/usr/bin/python3
# Calculator project
# Created a calculator that does basic arithmetic.
import math
contin = True
accum = 0.0
while contin:
        print("accum = ",accum)
        print('Please choose one of the following options: ')
        print("1) Addition")
        print("2) Subtraction")
        print("3) Multiplication")
        print("4) Division")
        print("5) Square root")
        print("6) Clear")
        print("0) Exit")
        opt = int(input("What is your option? "))
        if opt == 0:
                contin = False
                print("Program finished")
        elif opt == 1:
                add = float(input("Enter a number: "))
                accum = add + accum
        elif opt == 2:
                sub = float(input("Enter a number: "))
                accum = accum - sub
        elif opt == 3:
                multi = float(input("Enter a number: "))
                accum = accum * multi
        elif opt == 4:
                div = float(input("Enter a number: "))
                accum = accum / div
        elif opt == 5:
                if accum > 0:
                        accum = math.sqrt(accum)
        elif opt == 6
                accum = 0.0
        else:
                print("Illegal option",opt,)
