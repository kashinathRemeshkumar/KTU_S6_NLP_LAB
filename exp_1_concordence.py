from nltk.corpus import gutenberg
from nltk.text import Text


corpus=gutenberg.words('austen-emma.txt')

text=Text(corpus)
text.concordance('world')