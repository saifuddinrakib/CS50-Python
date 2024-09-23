import re

email= input ("what's your email?").strip()

#. means any charracter
#..
#if re.search (r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
if re.search (r"^\w+@\W+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
