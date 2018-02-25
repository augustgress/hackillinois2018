import json,csv,sqlite3,requests,random
from requests.exceptions import HTTPError
from random import choice
from string import ascii_lowercase
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

doc = []
with open("Users/users.txt", "r") as data:
    a = ""
    for line in data:
        if line[:5] == "DOCUM":
            doc.append(line[10:])

tfidf = TfidfVectorizer().fit_transform(doc)
cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
matches = sorted(range(len(cosine_similarities)), key=lambda i:cosine_similarities[i])[::-1][1:4]
for i in range(len(matches)):
    matches[i] += 1
print(cosine_similarities)
print(matches)


# with open("Doctest.txt", "r") as data:
#     a = ""
#     for line in data:
#         if line == "\n":
#             doc.append(a)
#             a = ""
#         a+= line
