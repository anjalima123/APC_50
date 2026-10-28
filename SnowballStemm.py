from nltk.stem import SnowballStemmer

ss = SnowballStemmer("english")

words = ["playing", "played", "plays", "running", "studies"]

for word in words:
    print(word, "->", ss.stem(word))