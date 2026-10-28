s = input("Enter a string: ")

max_count = 0
most = ""

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        most = ch

print("Most frequent character:", most)
print("Frequency:", max_count)