import re

name= input ("what's your name?").strip()

matches= re.search (r"^(.+), (.+)$",name)

if matches:
    first=matches.groups(1)
    last=matches.groups(2)
    name=f"{first} {last}"
print(f"hello, {name}")
