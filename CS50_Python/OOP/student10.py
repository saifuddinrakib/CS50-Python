class Student:

    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        self.name=name
        self.house=house


    def __str__(self):
        return (f"{self.name} from {self.house}")

    #getter
    @property
    def house(self):
        return self._house

    #setter
    @house.setter
    def house(self, house):
        if house not in ["Dhaka", "comilla", "chittagong", "rajshahi"]:
            raise ValueError ("Invalid House" )
        self._house=house


def main():
    student= get_student() 
    print(student)



def get_student():
    name = input("Name: ")
    house = input("House:" )
    return Student(name,house)


if __name__== "__main__":
    main()
