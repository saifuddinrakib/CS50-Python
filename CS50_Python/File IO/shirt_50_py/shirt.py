import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    #open the image
    try:
          imagefile = Image.open(sys.argv[1])
    #open shirt
    except FileNotFoundError:
          sys.exit("File does not exist")

    #get the size of the shirt
    shirtfile=Image.open ("shirt.png")

    size=shirtfile.size
    #paste shirt in muppet
    muppet= ImageOps.fit (imagefile,size)
    muppet.paste(shirtfile, shirtfile)

    #create output image
    muppet.save(sys.argv[2])

def check_command_line_arg():
        # Check the number of elements in the command line
        if len(sys.argv) < 3:
              sys.exit("Too few command-line arguments")
        if len(sys.argv) > 3:
              sys.exit("Too many command-line arguments")
        file1 = splitext(sys.argv[1])
        file2 = splitext(sys.argv[2])
        #check if it is a image file
        if check_extension (file1[1])== False:
              sys.exit("Invalid input")
        if check_extension (file2[1])==False:
              sys.exit("Invalid output")

        # Check if the arguments are CSV files

        if file1[1].lower() != file2[1].lower():

            sys.exit ("Input and output have different extensions")


def check_extension(file):
        if file in [ ".jpg", ".jpeg",".png"]:
              return True
        return False



#def check_extension(file):

if __name__ == "__main__":
    main()
