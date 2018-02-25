import os
import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


engine = create_engine('sqlite:///:memory:', echo=True)


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PkeyGCP.json"
import google.cloud.storage

def addCloud(source_file_name):
# Create a storage client.
    storage_client = google.cloud.storage.Client()

    # TODO (Developer): Replace this with your Cloud Storage bucket name.
    bucket_name = 'userpictures1'
    bucket = storage_client.get_bucket(bucket_name)

    # TODO (Developer): Replace this with the name of the local file to upload.
    #source_file_name = './hike.jpg'
    blob = bucket.blob(os.path.basename(source_file_name))

    # Upload the local file to Cloud Storage.
    blob.upload_from_filename(source_file_name)

    #print('File {} uploaded to {}.'.format(
    #source_file_name,
    #bucket))
    return("https://storage.googleapis.com/userpictures1/" + source_file_name)

    #export GOOGLE_APPLICATION_CREDENTIALS="./PkeyGCP.json"
print(addCloud("hike.jpg"))



def returnTopThree(index):
    docs = []
    conn = engine.connect()
    s = select([users])
    result = conn.execute(s)
    for row in result:
        docs.append(row["docs"])
    tfidf = TfidfVectorizer().fit_transform(doc)
    cosine_similarities = linear_kernel(tfidf[5:6], tfidf).flatten()
    matches = sorted(range(len(a)), key=lambda i:a[i])[::-1][1:]

def removeAndUpdate(url):

def addAndUpdate(source_file_name):
    addCloud(source_file_name)


def createUserTags():


#INSERT INTO users(firstname, lastname, email, birthday, sex, orientation, location, address, pwdhash, image, private, tags, matched, flag, priv)
