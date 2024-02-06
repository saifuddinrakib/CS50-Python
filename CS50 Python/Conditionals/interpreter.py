


# Get the expression
x , y , z = input("Expression: ").strip().split()

# Change type of variable x and z
x = float(x)
z = float(z)

# Perform the operations
match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "/":
        print(x / z)
    case "*":
        print(x * z)
#new_x = float(x)
#new_z = float(z)

#if y == "+":
#    result = new_x + new_z
#if y == "-":
#   result = new_x - new_z
#if y == "*":
#    result = new_x * new_z
#if y == "/":
#    result = new_x / new_z
#print(round(result,1))

