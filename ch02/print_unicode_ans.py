#!/usr/bin/env python3
import sys
import unicodedata

def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0:-<40}".format(""))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")

        if name_contains_words(name.lower(), words):
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))

        code += 1

def name_contains_words(name, words):
    for word in words:
        if not word in name:
            return False
            
    return True    

words = None

if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0])) 
        words = []
    else:
        words = sys.argv[1:]

if words != 0:
    print_unicode_table(words)   
    
