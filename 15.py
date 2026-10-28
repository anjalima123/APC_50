s = input("Enter a string: ")
for ch in s:
    count = 0
    for x in s:
        if ch == x:
            count += 1
    if count > 1:
        print(ch)