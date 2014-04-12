#!/usr/bin/env python3

def sort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    left = []
    right = []

    i = 1
    while i < len(list):
        if list[i] < pivot:
            left += [list[i]]
        else:
            right += [list[i]]

        i += 1

    return sort(left) + [pivot] + sort(right)

def median(list):
    median_index = len(list) // 2
    sorted_list = sort(list)

    if len(list) // 2 * 2 != len(list):
        return sorted_list[median_index]

    return (sorted_list[median_index - 1] + sorted_list[median_index]) / 2

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
    "highest =", highest, "mean =", total / len(numbers), "median =", median(numbers))
