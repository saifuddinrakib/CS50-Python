#create menu dictorinary
menu= {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#set current price to 0
total_amount=0
#loop forever
while True:
    try:
        #get user input
        item=input("Item: ").title()
    #check if item is already in the dictionary
        if item in menu:
    #add the item proce to current price
            total_amount +=menu[item]
    #print the current price
            print("Total: $", end="")
            print("{:.2f}".format(total_amount))
    except EOFError:
        #price a line and stop the loop
        print()
        break