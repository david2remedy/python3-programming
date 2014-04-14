#!/usr/bin/env python3
import sys

def read_data(filename):
    lines = []
    fh = None

    try:
        fh = open(filename, encoding="utf8")

        for line in fh:
            if line.strip():
                lines.append(line)

    except (IOError, OSError) as err:
        print(err)
        return []

    finally:
        if fh is not None:
            fh.close()

    return lines


def write_data(lines, filename):
    fh = None

    try:
        fh = open(filename, "w", encoding="utf8")

        for line in lines:
            fh.write(line)

    except (IOError, OSError) as err:
        print(err)

    finally:
        if fh is not None:
            fh.close()


def change_extension(filename, new_ext):
    last_dot_index = filename.rfind(".")
    return "{0}.{1}".format(filename[:last_dot_index], new_ext)


if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
    print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
    sys.exit()

for filename in sys.argv[1:]:
    lines = read_data(filename)

    if lines:
        write_data(lines, change_extension(filename, "ns"))
