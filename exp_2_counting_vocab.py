import nltk

text="welcome to the the world"
words=nltk.word_tokenize(text)

num_words=len(words)
unique_words=len(set(words))
perc_uniq_words=(unique_words/num_words)*100

print(f"number of words {num_words}\n number of different words {unique_words} \n percentage of unique words {perc_uniq_words}")