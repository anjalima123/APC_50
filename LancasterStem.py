from nltk.stem import LancasterStemmer

ls = LancasterStemmer()

words = ["playing", "played", "plays", "running", "studies"]

for word in words:
    print(word, "->", ls.stem(word))