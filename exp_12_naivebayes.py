from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


dataset=pd.read_csv('spam.csv',encoding='latin-1')

x=dataset['v2']
y=dataset['v1']


x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=4,test_size=0.2)

vectorizer=CountVectorizer()
x_train=vectorizer.fit_transform(x_train)
x_test=vectorizer.transform(x_test)

svm_model=SVC()
svm_model.fit(x_train,y_train)
svm_pred=svm_model.predict(x_test)
svm_acc=accuracy_score(y_test,svm_pred)
print(f'accuracy of svm {svm_acc}')

nb_model=MultinomialNB()
nb_model.fit(x_train,y_train)
nb_pred=nb_model.predict(x_test)
nb_acc=accuracy_score(y_test,nb_pred)

print(f'accuracy of naive bayes {nb_acc}')
