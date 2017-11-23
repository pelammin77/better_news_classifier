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
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
import pickle
from clean_data import clean_data


data = pd.read_csv("csv/data.csv",  encoding='cp1252')
article_text = data['article'].tolist()
article_category = data['category'].tolist()

#print(data.head())

for i,value in enumerate(article_text):
    print ("cleaning data:",i)
    article_text[i] = ' '.join([Word(word).lemmatize() for word in clean_data(value).split()])

vect = TfidfVectorizer(stop_words='english',min_df=2)
X = vect.fit_transform(article_text)
Y = np.array(article_category)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.20, random_state=50)

print("training size", X_train.shape)
print("Testing size:", X_test.shape)


model = RandomForestClassifier(n_estimators=300, max_depth=150,n_jobs=1)
model.fit(X_train, Y_train)

y_pred = model.predict(X_test)
c_mat = confusion_matrix(Y_test,y_pred)
kappa = cohen_kappa_score(Y_test,y_pred)
acc = accuracy_score(Y_test,y_pred)
print("Confusion Matrix:\n", c_mat)
print( "\nKappa: ",kappa)
print("\nAccuracy: ",acc)

with open('pkl/news_classifier.pkl','wb') as f:
    pickle.dump(model,f)
print("Model has saved file: pkl/news_classifier.pkl" )
with open("pkl/vect.pkl", 'wb') as f:
    pickle.dump(vect,f)
print("Word vectors has saved file: pkl/vect.pkl")
