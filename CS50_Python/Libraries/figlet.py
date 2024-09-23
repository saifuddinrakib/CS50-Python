import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
else:
    isRandomFont = False
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
    else:
        print("Invalid Usage")
        sys.exit(1)

if not isRandomFont:
    try:
        figlet.setFont(font=font_name)
    except:
        print("Invalid Font")
        sys.exit(1)

msg = input("Input: ")
try:
    rendered_text = figlet.renderText(msg)
    print(rendered_text)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
