def main():
    #name, house= get_student()
    student= get_student()
    #print (f"{name} from {house}")
    print (f"{student[0]} from {student[1]}")

def get_student():
    name=input ("Name:")
    house=input ("House: ")
    return (name, house)

if __name__== "__main__":
    main()
