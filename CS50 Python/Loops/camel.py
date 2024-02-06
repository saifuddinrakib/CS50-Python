#Get usr input
camelCase= input("camelCase: ")

#Print Snake_case
print("snake_case:", end="")
#loop thorugh every letter
for letter in camelCase:
    #check the letter is upppercase
    if letter.isupper():
        print("_" +letter.lower(), end="")
    else:
        print(letter, end="")
print()