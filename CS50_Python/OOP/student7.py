class Student:

    #instance method for making empty object
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dhaka", "comilla", "chittagong", "rajshahi"]:
            raise ValueError ("Invalid House" )
        self.name=name
        self.house=house


    def __str__(self):
        return (f"{self.name} from {self.house}")
#called it variables to object

def main():
    #name, house= get_student()
    student= get_student()
    print(student)

    #print (f"{name} from {house}")
    #print (f"{student.name} from {student.house}")
    # They are just called variables "name and called "house" inside of an object whose type is student.

def get_student():
    name = input("Name: ")
    house = input("House:" )
    return Student(name,house)




if __name__== "__main__":
    main()
