#!/usr/bin/env python3
import string
import sys
import collections

words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"

def by_value(item):
    return item[1]

for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)

            if len(word) > 2:
                words[word] += 1

for word, frequency in sorted(words.items(), key=by_value):
    print("'{0}' occurs {1} times".format(word, frequency))
