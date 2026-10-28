text = input("Enter message: ")
shift = int(input("Enter shift value: "))

result = ""

for ch in text:
    if ch.isalpha():
        result += chr(ord(ch) + shift)
    else:
        result += ch

print("Encrypted message:", result)