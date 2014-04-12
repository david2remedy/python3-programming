#!/usr/bin/env python3
import sys
import random

Articles = ["the", "a", "another"]
Subjects = ["cat", "dog", "man", "woman", "horse", "boy"]
Verbs = ["sang", "ran", "jumped", "laughed", "hoped"]
Adverbs = ["loudly", "quietly", "well", "badly", "rudely"]

def get_line_count():
    try:
        line_count = int(sys.argv[1])

        if not 1 <= line_count <= 10:
            print("line number must be between 1 and 10")
            return 0

        return line_count

    except ValueError:
        print("usage: awfulpoetry2.py [number]")
        return 0

    except IndexError:
        return 5

line_count = get_line_count()

i = 0
while i < line_count:
    line = random.choice(Articles)
    line += " " + random.choice(Subjects)
    line += " " + random.choice(Verbs)

    if (random.randint(0, 1)):
        line += " " + random.choice(Adverbs)

    print(line)
    i += 1
