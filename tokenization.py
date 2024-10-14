import nltk


nltk.download("punkt_tab")
nltk.download("punkt")
from nltk.tokenize import word_tokenize

text = "Hello, welcome to the world of NLP!"
tokens = word_tokenize(text)
print(tokens)