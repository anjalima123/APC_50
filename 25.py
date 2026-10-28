s = input("Enter a string: ")

frequency = {}

for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1

values = list(frequency.values())
values.sort(reverse=True)

if len(values) < 2:
    print("Second most frequent character not found")
else:
    second = values[1]

    for ch in frequency:
        if frequency[ch] == second:
            print("Second most frequent character:", ch)
            break