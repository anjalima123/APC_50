s = input("Enter a string: ")

checked = ""

for ch in s:
    if ch not in checked:
        count = 0

        for x in s:
            if ch == x:
                count += 1

        print(ch, "=", count)
        checked += ch