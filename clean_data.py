""""
file clean_data.py
author Petri Lamminaho
Cleans given string
"""

import re

def clean_data(data):

    string = re.sub(r"\'s", "", data)
    string = re.sub(r"\'ve", "", data)
    string = re.sub(r"n\'t", "", data)
    string = re.sub(r"\'re", "", data)
    string = re.sub(r"\'d", "", data)
    string = re.sub(r"\'ll", "", data)
    string = re.sub(r",", "", data)
    string = re.sub(r"!", " ! ", data)
    string = re.sub(r"\(", "", data)
    string = re.sub(r"\)", "", data)
    string = re.sub(r"\?", "", data)
    string = re.sub(r"'", "", data)
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", data)
    string = re.sub(r"[0-9]\w+|[0-9]", "", data)
    string = re.sub(r"\s{2,}", " ", data)
    return string.strip().lower()
