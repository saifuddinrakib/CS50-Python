#get the user input
answer=input("Input: ")

print("Output: ",end="")
#loop through every strings
for letter in answer:
    if not letter.lower() in ['a','e','i','o','u']:
        print(letter, end="")
print()