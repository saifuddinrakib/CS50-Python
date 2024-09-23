def main():
    #name, house= get_student()
    student= get_student()

    #print (f"{name} from {house}")
    print (f"{student['name']} from {student['house']}")

def get_student():

    student={}
    student["name"]=input("Name: ")
    student["house"]=input("house: ")
    return student

if __name__== "__main__":
    main()
