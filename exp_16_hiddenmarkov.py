from nltk import word_tokenize
from nltk.corpus import brown
from nltk.tag import hmm



dataset=brown.tagged_sents(tagset='universal')

trainer=hmm.HiddenMarkovModelTrainer()
model=trainer.train_supervised(dataset)

def tagging(text):
    tokens = word_tokenize(text)  # Tokenize the input text
    tagged = model.tag(tokens)  # Tag the entire sentence at once
    return tagged

text="Hello my name is Kashi."
print(tagging(text))