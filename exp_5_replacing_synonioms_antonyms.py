from nltk.corpus import wordnet,stopwords,sentiwordnet
from nltk.tokenize import word_tokenize



def replace(text):
    tokens=word_tokenize(text)
    stop_words=set(stopwords.words('english'))

    for i in range(len(tokens)):
        if tokens[i] not in stop_words:
            synset=list(sentiwordnet.senti_synsets(tokens[i]))
            #print(synset[0])

            if synset:
                syn=synset[0]
                pos=syn.pos_score()
                neg=syn.neg_score()
                syns=wordnet.synsets(tokens[i])

                if pos>=neg: #positive
                    print(tokens[i])
                    synonym=syns[0].lemmas()[0].name()
                    if synonym:
                        tokens[i]=synonym
                    

                else: #negative
                    anto=syns[0].lemmas()[0].antonyms()[0].name()
                    if anto:              
                        tokens[i]=anto





    final_text=' '.join(tokens)
    print(final_text)

replace('This is a bad running example')
            
