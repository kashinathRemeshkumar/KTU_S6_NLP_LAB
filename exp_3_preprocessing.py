import nltk

#nltk.download('stopwords')
#nltk.download('words')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords,words
from nltk.stem import PorterStemmer

text='this is a sample text that we use to @## demonstrate 123.'

tokens=word_tokenize(text)
stop_words=set(stopwords.words('english'))
stemmer=PorterStemmer()
alpha_tokens=[token.lower() for token in tokens if token.isalpha()]

english_words=set(words.words())
valid_token=[token for token in alpha_tokens if token in english_words]
filtered_tokens=[token for token in valid_token if token not in stop_words]
stemmer_tokens=[stemmer.stem(token) for token in filtered_tokens]

print("original text ",text)
print('Tokenized text',tokens)
print('filtered text',filtered_tokens)
print('stemmed_tokens ',stemmer_tokens)
print('alpha tokens',alpha_tokens)

