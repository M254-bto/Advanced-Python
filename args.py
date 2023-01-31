import sys
import getopt

filename = 'text.txt'
text = "Hello"


opts, args = getopt.getopt(sys.argv[1:], "f:m:", ["filename", "message"])

for opt, arg in opts:
    if opt == "-f":
        filename = arg
    if opt == "-m":
        text = arg

with open(filename, 'w+') as f:
    f.write(text)
