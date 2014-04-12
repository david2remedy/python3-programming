#!/usr/bin/env python3

numbers = []
total = 0
lowest = 1000000
highest = -1000000

while True:
    try:
        line = input("enter a number of Enter to finish: ")

        if not line:
            break

        number = int(line)
        numbers += [number]
        total += number

        if number > highest:
            highest = number

        if number < lowest:
            lowest = number

    except ValueError as err:
        print(err)

print("numbers:", numbers)
print("count =", len(numbers), "sum =", total, "lowest =", lowest, 
    "highest =", highest, "mean =", total / len(numbers))
