names=[]

with open ("names.txt") as file:
    #first check the file and then add the line in a order.
    for line in file:
        names.append (line.rstrip())

for name in sorted(names, reverse =True):
#for reverse sorted
    #sorted (iterable, / , key=None, reverse =false)

    print(f" Bonjour, {name}")
