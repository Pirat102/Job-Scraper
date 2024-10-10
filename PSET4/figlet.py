import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()




if len(sys.argv) >= 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in fonts:
        set_font = figlet.setFont(font=sys.argv[2])
        x = input("Input: ")
        print(figlet.renderText(x))
    else:
        sys.exit("Invalid usage")
elif len(sys.argv) == 1:
    set_font = figlet.setFont(font=choice(fonts))
    x = input("Input: ")
    print(figlet.renderText(x))


