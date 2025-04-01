from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def find_similar(text,query):
    vectorizer=TfidfVectorizer()
    vectorizer.fit_transform(text+[query])

    wordlist=[]
    rank_word=[]
    
    for i in range(len(text)):
        vec1=vectorizer.transform([text[i]])
        vec2=vectorizer.transform([query])
        similarity=cosine_similarity(vec1,vec2)
        wordlist.append(text[i])
        rank_word.append(similarity)
    
    m=0
    index=0
    for i in range(len(rank_word)):
        if rank_word[i]>=m:
            index=i
            
    return(f'{wordlist[index]}\n similarity {rank_word[index]}')





text1 = [
    "Machine learning is fascinating.",
    "I love deep learning.",
    "Natural language processing is a subfield of AI."
]

file=open('text.txt',mode='r')
text=file.readlines()
print(text)

query = "I am interested in Natural language processing and AI."

print(find_similar(text,query))

