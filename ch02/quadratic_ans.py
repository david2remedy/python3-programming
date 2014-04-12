#!/usr/bin/env python3
import cmath
import math
import sys

def get_float(message, allow_zero):
    x = None
    while x is None:
        try:
            x = float(input(message))
            if not allow_zero and abs(x) < sys.float_info.epsilon:
                print("zero is not allowed")
                x = None

        except ValueError as err:
            print(err)

    return x

def format_number(number, suffix):
    if number == 0:
        return ""

    if number < 0:
        return " - {0}{1}".format(-number, suffix)

    return " + {0}{1}".format(number, suffix)


print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("enter a: ", False)
b = get_float("enter b: ", True)
c = get_float("enter c: ", True)

x1 = None
x2 = None
discriminant = (b ** 2) - (4 * a * c)

if discriminant == 0:
    x1 = -(b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)

    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equation = "{}x\N{SUPERSCRIPT TWO}".format(a)
equation += "{}{} = 0".format(format_number(b, "x"), format_number(c, ""))
equation += " \N{RIGHTWARDS ARROW} x = {}".format(x1)

if x2 is not None:
    equation += " or x = {0}".format(x2)

print(equation)
