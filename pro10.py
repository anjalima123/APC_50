gender = input("Enter gender (male/female): ").lower()
marital = input("Enter marital status (married/unmarried): ").lower()
age = int(input("Enter age: "))

if marital == "married":
    print("Driver is insured.")
elif marital == "unmarried":
    if gender == "male" and age > 30:
        print("Driver is insured.")
    elif gender == "female" and age > 25:
        print("Driver is insured.")
    else:
        print("Driver is not insured.")
else:
    print("Invalid marital status.")
print()
input("Press Enter to exit...")