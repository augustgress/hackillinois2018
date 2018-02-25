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

def addCloud(source_file_names, index):
    # Create a storage client.
    source_file_names.strip()
    source_file_name_list = source_file_names.split(" ")
    storage_client = google.cloud.storage.Client()
    bucket_name = 'userpictures1'
    bucket = storage_client.get_bucket(bucket_name)
    subscription_key = "1ce10fd9a4b142f9b31c020ec61d2393"
    assert subscription_key
    for source_file_name in source_file_name_list:
        blob = bucket.blob(os.path.basename(source_file_name))
        # Upload the local file to Cloud Storage.
        blob.upload_from_filename(source_file_name)
        url = ("https://storage.googleapis.com/userpictures1/" + source_file_name)
        vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
        vision_analyze_url = vision_base_url + "analyze"
        doc = ""
        try:
            headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
            params   = {'visualFeatures': 'Tags'}
            data     = {'url': url}
            response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
            response.raise_for_status()
            analysis = response.json()
            for ele in analysis["tags"]:
                intWeight = int(round(ele["confidence"]*10))
                tag = ele["name"]+ " "
                for i in range(intWeight):
                    doc += tag
            if "person" in doc:
                con = None
                con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
                cur = con.cursor()
                tempPrivate = ""
                cur.execute("SELECT * FROM users WHERE Id=%s", (index))
                row = cur.fetchone()
                tempPrivate += row[10]
                tempPrivate += url + " "
                cur.execute("UPDATE users SET private=%s WHERE Id=%s", (tempPrivate, index))
                con.commit()
            else:
                con = None
                con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
                cur = con.cursor()
                tempPublic = ""
                cur.execute("SELECT * FROM users WHERE Id=%s", (index))
                row = cur.fetchone()
                tempPublic += row[9]
                tempPublic += url + " "
                cur.execute("UPDATE users SET image=%s WHERE Id=%s", (tempPublic, index))
                con.commit()
        except:
            print("damn")
        finally:
            if con:
                con.close()


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





import requests,random
from requests.exceptions import HTTPError

def addAndUpdate(source_file_name, index):
   url = addCloud(source_file_name)
   subscription_key = "1ce10fd9a4b142f9b31c020ec61d2393"
   assert subscription_key
   vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
   vision_analyze_url = vision_base_url + "analyze"
   doc = ""
   try:
       headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
       params   = {'visualFeatures': 'Tags'}
       data     = {'url': URL}
       response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
       response.raise_for_status()
       analysis = response.json()
       for ele in analysis["tags"]:
           intWeight = int(round(ele["confidence"]*10))
           tag = ele["name"]+ " "
           for i in range(intWeight):
               doc += tag
       if "person" in doc:
           con = None
           docs = []
           con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
           cur = con.cursor()
           tempPrivate = ""
           cur.execute("SELECT * FROM users WHERE Id=%s", (index))
           row = cur.fetchone()
           tempPrivate += row[10]
           tempPrivate += url + " "
           cur.execute("UPDATE users SET private=%s WHERE Id=%s", (tempPrivate, index))
           con.commit()
       else:
           con = None
           docs = []
           con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
           cur = con.cursor()
           tempPublic = ""
           cur.execute("SELECT * FROM users WHERE Id=%s", (index))
           row = cur.fetchone()
           tempPublic += row[9]
           tempPublic += url + " "
           cur.execute("UPDATE users SET image=%s WHERE Id=%s", (tempPublic, index))
           con.commit()
   except:
       print("damn")
   finally:
       if con:
           con.close()






#def createUserTags():


#INSERT INTO users(firstname, lastname, email, birthday, sex, orientation, location, address, pwdhash, image, private, tags, matched, flag, priv)
