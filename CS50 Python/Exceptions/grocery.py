#create empty dictionary
grocery={}
#loop forever
while True:
    try:
        #get user input
        item=input().lower()
        #check if item is already in dictionary
        if item in grocery:
        #if it is, add 1 in the count
            grocery[item] +=1
        #otherwise, add the items for the first time
        else:
            grocery[item]=1
    except EOFError:

        #print all the items in alphabetical order
        for key in sorted (grocery.keys()):
            print(grocery[key],key.upper())
           #stop the while loop
        break