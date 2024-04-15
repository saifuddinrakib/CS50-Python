class Student:
    ...


def main():
    #name, house= get_student()
    student= get_student()

    #print (f"{name} from {house}")
    print (f"{student.name} from {student.house}")
    # They are just called variables "name and called "house" inside of an object whose type is student.

def get_student():
    name = input("Name: ")
    house = input("House:" )
    student= Student(name,house)
    return student



if __name__== "__main__":
    main()
