from nltk.util import ngrams
from collections import defaultdict,Counter
from nltk.tokenize import word_tokenize

def train_ngrams(text,n):
    tokens=word_tokenize(text.lower())
    ngram=list(ngrams(tokens,n))

    model=defaultdict(Counter)

    for n_gram in ngram:
        prefix,suffix=tuple(n_gram[:-1]),n_gram[-1]
        model[prefix][suffix]+=1

    for prefix,suffix_count in model.items():
        total=sum(suffix_count.values())
        probabilities={}

        for word,count in suffix_count.items():
            prob=count/total
            probabilities[word]=prob
        model[prefix]=probabilities
    return model


def predict_next(model,text,n):
    tokens=word_tokenize(text.lower())
    prefix=tuple(tokens[-(n-1):])

    if prefix in model:
        print(model[prefix])


text = "this is a simple text to demonstrate the n gram model and it works well"
trigram_model = train_ngrams(text, 3)

input_sequence = "simple text to"
predict_next(trigram_model, input_sequence, 3)

