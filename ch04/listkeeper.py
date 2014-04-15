#!/usr/bin/env python3
import os

EXTENSION = ".lst"

def main():
    filename = get_list_file_name()
    items = read_items(filename)
    modified = False

    while True:
        print_items(items)
        action = get_choice("[A]dd  [D]elete  [S]ave  [Q]uit", default="a", options="AaDdSsQq").lower()

        if action == "a":
            add_new_item(items)
            modified = True

        elif action == "d":
            delete_item(items)
            modified = True

        elif action == "s":
            save_file(filename, items)
            print("Saved {0} items to {1}".format(len(items), filename))
            modified = False

        elif action == "q":
            if modified and confirm_save():
                save_file(filename, items)
            break


def get_list_file_name():
    files = get_files()
    return choose_file(files) if files else create_new_file()


def get_files():
    all_files = os.listdir(".")
    return sorted([f for f in all_files if f.endswith(EXTENSION)])


def create_new_file():
    name = get_string("Choose file name", "file name")
    name += EXTENSION if not(name.endswith(EXTENSION)) else ""
    save_file(name, [])

    return name


def read_items(filename):
    fh = None

    try:
        fh = open(filename, encoding="utf8")
        return [line.strip() for line in fh]

    finally:
        if fh is not None:
            fh.close()


def print_items(items):
    print()
    if items:
        print_list(items, separator=":")
    else:
        print("-- no items are in the list --")


def choose_file(files):
    print_list(files)
    choice = get_integer("Choose file (1-{0}) (0 to create)".format(len(files)), maximum=len(files))

    if choice == 0:
        return create_new_file()

    return files[choice - 1]


def add_new_item(items):
    items.append(get_string("Add item", "item"))
    items.sort()


def delete_item(items):
    item_to_delete = get_integer("Delete item number (or 0 to cancel)", maximum=len(items))

    if item_to_delete > 0:
        del items[item_to_delete - 1]


def save_file(filename, items):
    fh = None

    try:
        fh = open(filename, "w", encoding="utf8")

        for item in items:
            fh.write(item + "\n")

    finally:
        if fh is not None:
            fh.close()


def confirm_save():
    return get_choice("Save unsaved changes? (y/n)", default="y", options="YyNn").lower() == "y"
    

def print_list(items, separator="."):
    for index, item in enumerate(items, start=1):
        print("{index}{separator} {item}".format(**locals()))


def get_choice(message, default, options):
    while True:
        try:
            response = input("{message} [{default}]: ".format(**locals()))

            if not response:
                return default

            if len(response) != 1 or response not in options:
                raise ValueError("choice must be one of '{0}'".format(options))

            return response

        except ValueError as err:
            print("ERROR", err)


def get_string(message, name):
    while True:
        try:
            line = input(message + ": ")

            if not line:
                raise ValueError("{0} may not be empty".format(name))

            return line

        except ValueError as err:
            print("ERROR", err)


def get_integer(message, minimum=0, maximum=100):
    class RangeError(Exception): pass

    while True:
        try:
            response = int(input(message + ": "))

            if not(minimum <= response <= maximum):
                raise RangeError("Invalid choice - must be between {minimum} and {maximum}".format(**locals()))

            return response

        except RangeError as err:
            print("ERROR", err)

        except ValueError:
            print("ERROR choice must be an integer")


main()
