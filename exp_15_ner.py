from nltk import word_tokenize,ne_chunk,pos_tag


'''nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')'''

sentence="Hello my name is Kashi,this is my friend Hari"

tokens=word_tokenize(sentence)
tagged=pos_tag(tokens)
named_entities=ne_chunk(tagged)

print(named_entities)

named=[]
for entity in named_entities:
    if hasattr(entity,'label'):
        name=entity.leaves()[0][0]
        named.append((name,entity.label()))

print(named)
