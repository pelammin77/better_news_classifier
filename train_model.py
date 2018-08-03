"""
file: train_model.py
author: Petri Lamminaho
reads csv file to pandas df
vectorizes words
split data to training and testing data
create, train and test the model
saves vectors and model to pkl files

"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import Word
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB


from sklearn import tree
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
import pickle
import os
from clean_data import clean_data
from sklearn.feature_extraction.text import CountVectorizer

data = pd.read_csv("csv/data.csv",  encoding='cp1252')
article_text = data['article'].tolist()
article_category = data['category'].tolist()

#print(data.head())

for i,value in enumerate(article_text):
    print ("cleaning data:",i)
    article_text[i] = ' '.join([Word(word).lemmatize() for word in clean_data(value).split()])

vect = TfidfVectorizer(stop_words='english',min_df=10)
#vect = CountVectorizer()
X = vect.fit_transform(article_text)
Y = np.array(article_category)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=50)

print("training size", X_train.shape)
print("Testing size:", X_test.shape)
from sklearn.linear_model import PassiveAggressiveClassifier


#model = RandomForestClassifier(n_estimators=300, max_depth=150,n_jobs=1) # accuracy over 96%
model = MultinomialNB()# acc over 98.1%
#model = RandomForestClassifier(n_estimators=300, max_depth=150,n_jobs=1) # accuracy over 96%
#model = PassiveAggressiveClassifier() # even better acc over 97%
#model = tree.DecisionTreeClassifier()

model.fit(X_train, Y_train)

predict = model.predict(X_test)

acc = accuracy_score(Y_test,predict)



print("\nAccuracy: ",acc)

pkl_directory = "pkl"
if not os.path.exists(pkl_directory):
    os.makedirs(pkl_directory)
with open(pkl_directory+'/news_classifier.pkl','wb') as f:
    pickle.dump(model,f)
print("Model has saved file: pkl/news_classifier.pkl" )
with open(pkl_directory+"/vect.pkl", 'wb') as f:
    pickle.dump(vect,f)
print("Word vectors has saved file: pkl/vect.pkl")
