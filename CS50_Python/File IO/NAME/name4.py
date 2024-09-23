with open ("names.txt", "r") as file:
           lines= file.readlines()

for line in lines:
        #lines as list and line is variable
        print("hello, ", line.rstrip())

        #rstrip makes it clearner
