patients = [
    ["Amit", 25],
    ["Priya", 30],
    ["Rahul", 40]
]
patients.append(["Neha", 28])
name = input("Search patient: ")
found = False
for patient in patients:
    if patient[0] == name:
        print("Patient found:", patient)
        found = True
if not found:
    print("Patient not found.")
patients.remove(patients[1])
print("All patients:")
for patient in patients:
    print(patient)
print("Total patients:", len(patients))