import sys
from pyfiglet import Figlet
from random import choice

def main():
    figlet = Figlet()
    all_fonts = figlet.getFonts()

    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in all_fonts:
            sys.exit("Invalid usage")

    s = input("Input: ")
    convert(s, figlet, all_fonts)

def convert(s, figlet, all_fonts):
    if len(sys.argv) == 1:
        figlet.setFont(font = choice(all_fonts))
        print(figlet.renderText(s))
    else:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(s))

main()
