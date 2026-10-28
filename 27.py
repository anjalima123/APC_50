salaries = [25000, 35000, 50000, 60000, 75000, 28000]
print("Highest salary:", max(salaries))
print("Lowest salary:", min(salaries))
print("Average salary:", sum(salaries) / len(salaries))
above_50000 = 0
below_30000 = 0
for salary in salaries:
    if salary > 50000:
        above_50000 += 1
    if salary < 30000:
        below_30000 += 1
print("Above ₹50,000:", above_50000)
print("Below ₹30,000:", below_30000)