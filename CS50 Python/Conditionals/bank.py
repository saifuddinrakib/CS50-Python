#get user input

answer = input("Greeting: ")

answer_lower = answer.lower().strip()
#check the answer if true or false for making a statement
if "hello" in answer_lower:
    print("$0")
elif "h"== answer_lower[0]:
    print("$20")
else:
    print("$100")