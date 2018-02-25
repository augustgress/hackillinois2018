import os
import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy #uses extention in this file
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel




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
    con = None
    docs = []
    try:
        con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
        cur = con.cursor()
        cur.execute("SELECT * FROM users")



        while(True):
            row = cur.fetchone()
            if (row == None):
                break
            docs.append(row[11])


    except psycopg2.DatabaseError, e:
        if con:
            con.rollback()

        print( 'Error %s' % e )
        sys.exit(1)

    finally:
        if con:
            con.close()

    tfidf = TfidfVectorizer().fit_transform(docs)
    cosine_similarities = linear_kernel(tfidf[index-1:index], tfidf).flatten()
    matches = sorted(range(len(cosine_similarities)), key=lambda i:cosine_similarities[i])[::-1][1:4]
    return matches

print(returnTopThree(5))


#def addAndUpdate(source_file_name):
#    url = addCloud(source_file_name)



#def createUserTags():


#INSERT INTO users(firstname, lastname, email, birthday, sex, orientation, location, address, pwdhash, image, private, tags, matched, flag, priv)
