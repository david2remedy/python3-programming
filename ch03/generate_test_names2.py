#!/usr/bin/env python3
import random

def get_forenames_and_surnames():
    forenames, surnames = [], []
    for names, filename in ((forenames, "data/forenames.txt"), (surnames, "data/surnames.txt")):
        for names in open(filename, encoding="utf8"):
            names.append(name.rstrip())

    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names2.txt", "w", encoding="utf8")

limit = 100
year = list(range(1970, 2013)) * 3

for year, forename, surname in zip(random.sample(years, limit), 
                                   random.sample(forenames, limit),
                                   random.sample(surnames, limit)):
    name = "{0} {1}".format(forename, surname)
    fh.write("{0:.<25}.{1}\n".format(name, year))
