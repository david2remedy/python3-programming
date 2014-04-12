#!/usr/bin/env python3
import random

Articles = ["the", "a", "another"]
Subjects = ["cat", "dog", "man", "woman", "horse", "boy"]
Verbs = ["sang", "ran", "jumped", "laughed", "hoped"]
Adverbs = ["loudly", "quietly", "well", "badly", "rudely"]

for i in (1,2,3,4,5):
    line = random.choice(Articles)
    line += " " + random.choice(Subjects)
    line += " " + random.choice(Verbs)

    if (random.randint(0, 1)):
        line += " " + random.choice(Adverbs)

    print(line)
