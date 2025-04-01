from nltk.corpus import treebank
from nltk.tag.sequential import ClassifierBasedPOSTagger
from nltk.tokenize import word_tokenize

train=treebank.tagged_sents()[:3000]
test=treebank.tagged_sents()[3000:]


model=ClassifierBasedPOSTagger(train=train)
print(f"accuracy {model.accuracy(test)}")


sentence="Hello my name is John."
sentence=word_tokenize(sentence)
print(model.tag(sentence))
