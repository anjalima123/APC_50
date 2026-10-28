numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for n in numbers:
    frequency[n] = frequency.get(n, 0) + 1
print(frequency)