class Student:

    def __init__(self,name,house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Dhaka", "comilla", "chittagong", "rajshahi"]:
            raise ValueError ("Invalid House" )
        self.name=name
        self.house=house
        self.patronus=patronus

    def __str__(self):
        return (f"{self.name} from {self.house}")


def main():
    student= get_student()
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House:" )
    patronus= input ("patronus: ")
    return Student(name,house,patronus)


if __name__== "__main__":
    main()
