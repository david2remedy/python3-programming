#!/usr/bin/env python3
import sys
import optparse
import xml.sax.saxutils

def main():
    parser = optparse.OptionParser()
    parser.add_option("-w", "--maxwidth", dest="maxwidth", type="int",
                      help=("the maximum number of characters that can be "
                            "output to string fields [default: %default]"))

    parser.add_option("-f", "--format", dest="format", 
                      help="the format used for outputting numbers [default: %default]")

    parser.set_defaults(maxwidth=100, format=".0f")
    opt, args = parser.parse_args()

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

            print_line(line, color, opt.maxwidth, opt.format)
            count += 1

        except EOFError:
            break

    print_end()


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
