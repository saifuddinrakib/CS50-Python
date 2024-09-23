students=[]
with open ("students.csv") as file:
    for line in file:
        name, house= line.rstrip().split(",")

        #students ["name"]=name & #students ["name"]=house
        student={"house": house, "name": name}
        students.append(student)
def get_name(student):
    return student ["name"]
    #key=lambda student: student["name"] instead of def
for student in sorted(students, key =get_name):
    print(f"{student['name']} is in {student['house']}")

