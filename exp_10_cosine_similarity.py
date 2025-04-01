from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

corpus=['this is the first document',
        'this is the second document']

vectorizer=TfidfVectorizer()
vectorizer.fit_transform(corpus)


vec1=vectorizer.transform([corpus[0]])
vec2=vectorizer.transform([corpus[1]])

similarity=cosine_similarity(vec1,vec2)
print(f'similarity of the documents {similarity}')