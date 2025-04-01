from sklearn.feature_extraction.text import CountVectorizer

corpus=["this is the first document",
        'this is the second documnet',
        'and this is the third document']

vectorzer=CountVectorizer()
x=vectorzer.fit_transform(corpus)


for i in range(len(corpus)):
    print(f"BoW representation of document({i+1}):{x[i].toarray()[0]}")
