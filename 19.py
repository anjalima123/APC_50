students = ["Amit", "Priya", "Rahul", "Neha"]
print("Total students:", len(students))
name = input("Search student: ")
if name in students:
    print(name, "is present.")
else:
    print(name, "is absent.")
students.append("Ravi")
students.remove("Neha")
print("Updated list:", students)