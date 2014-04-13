#!/usr/bin/env python3
import sys
import collections

ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)
User = collections.namedtuple("User", "username forename middlename surname id")

def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}

    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()

            if line:
                user = process_line(line, usernames)
                users[(user.surname.lower(), user.forename.lower(), user.id)] = user

    print_users(users)

def process_line(line, usernames):
    fields = line.split(":")
    username = generate_username(fields, usernames)

    return User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])

def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + 
                 fields[MIDDLENAME][:1] + 
                 fields[SURNAME]).replace("-", "").replace("'", ""))

    username = original_name = username[:8].lower()
    count = 1

    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1

    usernames.add(username)
    return username

def print_users(users):
    name_width = 17
    username_width = 9

    title = "{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=name_width, uw=username_width)
    dashes = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=name_width, uw=username_width)

    details = []

    for key in sorted(users):
        user = users[key]
        initial = ""

        if user.middlename:
            initial = " " + user.middlename[0]

        name = "{0.surname}, {0.forename}{1}".format(user, initial)
        details += ["{0:.<{nw}.{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=name_width, uw=username_width)]

    if len(details) % 2 != 0:
        details += [""]

    for i in range(0, len(details), 64):
        chunk = details[i:i + 64]

        if i > 0:
            print("")

        print("{0}  {0}".format(title))
        print("{0}  {0}".format(dashes))

        for first_details, second_details in zip(chunk[::2], chunk[1::2]):
            print("{0}  {1}".format(first_details, second_details))

main()
