from sklearn.feature_extraction.text import TfidfVectorizer


vectorizer=TfidfVectorizer()

corpa=['this is the first document',
       'this is another document',
       'this is the third document']

tfidf_matrix=vectorizer.fit_transform(corpa)


tfidf_matrix=tfidf_matrix.toarray()
print(tfidf_matrix)
feature_name=vectorizer.get_feature_names_out()
print(feature_name)

for i in range (len(corpa)):
    print(f"Document {i+1}")
    for j in range (len(feature_name)):
        print(f"{feature_name[j]} = {tfidf_matrix[i][j]}")  
    print()  

