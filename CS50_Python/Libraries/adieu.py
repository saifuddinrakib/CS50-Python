import inflect

p = inflect.engine()
names = []

# Loop indefinitely
while True:
    try:
        # Get user input
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # Create a new line and stop the loop
        print()
        break

# Printing using inflect module
output = p.join(names)
print("Adieu, adieu, to " + output)
