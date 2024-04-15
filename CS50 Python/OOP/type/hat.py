import random


class Hat:

    #This is the constructor method for the 'Hat' clas
    def __init__(self):
        self.houses=["dhaka", "comilla", "chattagram", "rajshahi"]
    #This line creates an instance variable called houses and assigns it a list containing the names of four cities


    def sort(self,name):
        #This defines a method named sort that takes two parameters: self (represents the instance of the class) and name ( represents a person's name).
        print(name,"is in", random.choice(self.houses))


hat=Hat()
hat.sort("Harry")




