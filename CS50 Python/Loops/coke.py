# Variable to keep track of the amount due
amount_due = 50

# Loop until amount_due is greater than 0
while amount_due > 0:

    # Print the amount due
    print("Amount Due:", amount_due)

    # Ask the user to insert a coin
    coin = int(input("Insert Coin: "))

    # Check if the inserted coin is valid (25, 10, or 5 cents)
    if coin in [25, 10, 5]:
        # Subtract the coin's value from amount_due
        amount_due -= coin
    else:
        print("Invalid coin. Please insert a valid coin (25, 10, or 5 cents).")

# Calculate the change owed
change_owed = abs(amount_due)
print("Change Owed:", change_owed)
