import sys

def main():
    # Check the command line arguments
    check_command_line_arg()

    # Try to open the file
    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

    # If not open the file, that means the file does not exist
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Loop through the lines
    count_lines = 0
    for line in lines:
        if not check_comment_or_empty_line(line):
            count_lines += 1

    print(count_lines)

# Function to check the command line
def check_command_line_arg():
    # Check the number of elements in the command line
    if len(sys.argv) != 2:
        sys.exit("Usage: python script.py filename.py")

    # Check if it is a Python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

# Function to check if the line is a comment or empty
def check_comment_or_empty_line(line):
    if line.isspace() or line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
