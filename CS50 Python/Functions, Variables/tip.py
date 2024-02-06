def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent

    print(tip)
# Print the calculated tip amount with two decimal places
    print(f"Leave ${tip:.2f}") # .2f: This is a formatting specification for floating-point numbers.


def dollars_to_float(d): #represents a dollar amount with a dollar sign
    d_without_dollar_sign=d.replace("$","")  # This line removes the dollar sign from the input string
    return float (d_without_dollar_sign)

def percent_to_float(p):
    p_without_percent=p.replace("%","")
    conversion_of_percent=float (p_without_percent)/100
    return conversion_of_percent

main()