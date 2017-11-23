"""
file: data2csv.py
author: Petri Lamminaho
Module converts data txt file to pandas dataframe and create the csv file
"""

import csv
import pandas as pd
import os
import codecs

folders = ["business", "entertainment", "politics", "science", "sport", "tech"]
data_folder = "bbc"
os.chdir(data_folder)
article_text = []
article_category = []

for i in folders:
    files = os.listdir(i)
    for text_file in files:
        file_path = i + "/" + text_file
        print("reading file:", file_path)
        with codecs.open(file_path,'r', "utf-8", errors='ignore') as f:
            data = f.readlines()
        data = ' '.join(data)
        article_text.append(data)
        article_category.append(i)

data = {'article': article_text, 'category': article_category}
df = pd.DataFrame(data)
#print(df.head())

print('create csv file')
df.to_csv("../csv/data.csv",index=False)