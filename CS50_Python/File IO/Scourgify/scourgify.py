import sys
import csv

def main():
    # Check the command line arguments
    check_command_line_arg()
    # create a variable to store the data
    output = []

    # Open the input CSV file
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].strip(), "last": split_name[0].strip(), "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write to the output CSV file
    try:
        with open(sys.argv[2], "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in output:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not write to {sys.argv[2]}")

# Function to check the command line arguments
def check_command_line_arg():
    # Check the number of elements in the command line
    if len(sys.argv) != 3:
        sys.exit("Usage: python script.py input.csv output.csv")

    # Check if the arguments are CSV files
    if not (sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv')):
        sys.exit("Both arguments must be CSV files.")

if __name__ == "__main__":
    main()
