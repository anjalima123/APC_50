marks = [60, 75, 80, 45, 90, 55, 70, 85, 65, 50,
         95, 72, 68, 88, 76, 40, 82, 91, 58, 73]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
above = 0
below = 0
for m in marks:
    if m > average:
        above += 1
    elif m < average:
        below += 1
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Above average:", above)
print("Below average:", below)