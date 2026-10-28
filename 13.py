s = input("Enter a sentence: ")
words = s.split()
shortest = words[rt0]
for word in words:
    if len(word) < len(shortest):
        shortest = word
print("Shortest word:", shortest)