#!/usr/bin/env python3
import os
import time

import os.path as path

from optparse import OptionParser


def main():
    parser = OptionParser(usage="Usage: %prog [options] [path1 [path2 [... pathN]]]",
                          description=("Lists entries in directories. "
                                       "The paths are optional; if not given . is used"))

    parser.add_option("-H", "--hidden", action="store_true", dest="show_hidden", 
                      help="show hidden files [default: off]")

    parser.add_option("-m", "--modified", action="store_true", dest="show_last_modified",
                      help="show last modified date/time [default: off]")

    order_choices = ["name", "n", "modified", "m", "size", "s"]

    parser.add_option("-o", "--order", dest="order", type="choice", default="name",
                      choices=order_choices,
                      help=("order by ({0}) [default: %default]".format(", ".join(
                        ["'{0}'".format(choice) for choice in order_choices]))))

    parser.add_option("-r", "--recursive", action="store_true", dest="recursive",
                      help="recurse into subdirectories [default: off]")

    parser.add_option("-s", "--size", action="store_true", dest="show_sizes",
                      help="show sizes [default: off]")

    options, args = parser.parse_args()
    directories = args if len(args) > 0 else ["."]

    print_all_entries(directories, options)


def print_all_entries(directories, options):
    total_files = total_directories = 0
    entries = []

    for directory in directories:
        entries += get_entries(directory, options)

    entries.sort(key=sort_key(options.order))

    for entry in entries:
        print(format_entry(entry, options))

        if path.isdir(entry):
            total_directories += 1
        else:
            total_files += 1

    print("{0} files, {1} directories".format(total_files, total_directories))


def get_entries(directory, options):
    if options.recursive is True:
        return get_entries_recursively(directory, options)

    entries = []
    for entry in os.listdir(directory):
        if not entry.startswith(".") or options.show_hidden is True:
            entries.append(path.join(directory, entry))

    return entries


def get_entries_recursively(directory, options):
    entries = []
    for root, dirs, files in os.walk(directory):
        if root != directory and path.basename(root).startswith(".") and not options.show_hidden is True:
            continue

        for entry in dirs + files:
            if not entry.startswith(".") or options.show_hidden is True:
                entries.append(path.join(root, entry))

    return entries;


def sort_key(order):
    if order in {"s", "size"}:
        return lambda e: path.getsize(e)

    if order in {"m", "modified"}:
        return lambda e: path.getmtime(e)

    return str


def format_entry(entry, options):
    line = ""

    if options.show_last_modified is True:
        line += time.strftime("%Y-%m-%d %H:%M:%S ", time.gmtime(path.getmtime(entry)))

    if options.show_sizes is True:
        line += "{0:>16,} ".format(path.getsize(entry))

    return line + entry + ("/" if path.isdir(entry) else "")


main()