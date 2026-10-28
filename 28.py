s = input("Enter a paragraph: ")

words = s.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

for word in frequency:
    print(word, "=", frequency[word])