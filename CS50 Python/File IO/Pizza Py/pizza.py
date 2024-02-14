import sys
import csv
from tabulate import tabulate

def main():
    # Check the command line arguments
    check_command_line_arg()
    # create a vairable to store the data
    table=[]
    #open the file

    try:
        with open (sys.argv[1], "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                table.append(row)
                print(row)
    # If not open the file, that means the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    #print the table
    print(tabulate(table[1:], headers=table[0],tablefmt="grid"))


# Function to check the command line
def check_command_line_arg():
    # Check the number of elements in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
     # Check if it is a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file" )

    # Check if it is a Python file

# Function to check if the line is a comment or empty


if __name__ == "__main__":
    main()
