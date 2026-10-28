temperature = [
    30, 32, 29, 35, 31, 28, 33, 36, 30, 34,
    29, 31, 37, 32, 30, 28, 35, 33, 31, 36,
    29, 34, 32, 30, 38, 31, 33, 35, 29, 32
]

hottest = max(temperature)
coldest = min(temperature)
average = sum(temperature) / len(temperature)
above = 0
below = 0
for t in temperature:
    if t > average:
        above += 1
    elif t < average:
        below += 1
print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)