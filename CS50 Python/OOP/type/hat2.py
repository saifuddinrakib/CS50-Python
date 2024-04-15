import random


class Hat:
    houses=["dhaka", "comilla", "chattagram", "rajshahi"]
    #This line creates an instance variable called houses and assigns it a list containing the names of four cities

    @classmethod
    def sort(cls,name):
        #This defines a method named sort that takes two parameters: self (represents the instance of the class) and name ( represents a person's name).
        print(name,"is in", random.choice(cls.houses))



Hat.sort("Harry")

