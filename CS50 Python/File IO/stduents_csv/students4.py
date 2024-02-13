import csv

students=[]

with open ("students2.csv") as file:
    #reader=csv.reader(file)
    reader=csv.DictReader(file)
    #for name, home in reader:
    for row in reader:


        #students ["name"]=name & #students ["name"]=house

        #students.append({"home": home, "name": name})
        students.append({"name": row ["name"], "home": row ["home"]})

    #key=lambda student: student["name"] instead of def
for student in sorted(students, key =lambda student: student ["name"]):
    print(f"{student['name']} is from {student['home']}")
