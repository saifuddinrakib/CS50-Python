import re

email= input ("what's your email?").strip()

#. means any charracter
#..
if re.search (r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
