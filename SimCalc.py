import json,csv,sqlite3,requests,random
from requests.exceptions import HTTPError
from random import choice
from string import ascii_lowercase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

doc = []
with open("Doctest.txt", "r") as data:
    a = ""
    for line in data:
        if line == "\n":
            doc.append(a)
            a = ""
        a+= line

tfidf = TfidfVectorizer().fit_transform(doc)
cosine_similarities = linear_kernel(tfidf[5:6], tfidf).flatten()
print(cosine_similarities)
