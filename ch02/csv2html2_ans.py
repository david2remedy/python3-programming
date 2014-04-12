#!/usr/bin/env python3
import sys
import xml.sax.saxutils

def main():
    options = process_options()

    if not options:
        return

    max_width = options[0]
    number_format = options[1]

    print_start()
    count = 0

    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"

            print_line(line, color, max_width, number_format)
            count += 1

        except EOFError:
            break

    print_end()

def process_options():
    max_width = 100
    format = ".0f"

    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage:\n"
                  "csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html\n\n"
                  "maxwidth is an optional integer; if specified, it sets the maximum\n"
                  "number of characters that can be output for string fields,\n"
                  "otherwise a default of 100 characters is used.\n\n"
                  "format is the format to use for numbers; if not specified it\n"
                  "defaults to \".0f\".")
            return None

        for arg in sys.argv[1:]:
            if arg.startswith("maxwidth="):
                max_width = int(arg.replace("maxwidth=", ""))
            elif arg.startswith("format="):
                format = arg.replace("format=", "")

    return (max_width, format)

def print_start():
    print("<table border='1'>")

def print_end():
    print("</table>")

def print_line(line, color, max_width, number_format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)

    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            
            try:
                x = float(number)
                print("<td align='right'>{{0:{0}}}</td>".format(number_format).format(round(x)))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                
                if len(field) <= max_width:
                    field = escape_html(field)
                else:
                    field = "{0} ...".format(escape_html(field[:max_width]))

                print("<td>{0}</td>".format(field))

    print("</tr>")

def extract_fields(line):
    fields = []
    field = ""
    quote = None

    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue

        if quote is None and c == ',':
            fields.append(field)
            field = ""
        else:
            field += c

    if field:
        fields.append(field)

    return fields

def escape_html(text):
    return xml.sax.saxutils.escape(text)

main()
