import os
import sqlalchemy
# from sqlalchemy import create_engine
# from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import psycopg2
from flask.ext.sqlalchemy import SQLAlchemy #uses extention in this file
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import glob
import os, shutil, os.path
from os import walk
from os import listdir
from os.path import isfile, join
import requests,random
from requests.exceptions import HTTPError


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PkeyGCP.json"
import google.cloud.storage

def imageNameToVStrings(index):
    f = []

    for (dirpath, dirnames, filenames) in walk('pics/'):
        f.extend(filenames)
        break


    return (addCloud(f, index))





def addCloud(source_file_names, index):
    # Create a storage client.
    storage_client = google.cloud.storage.Client()
    bucket_name = 'userpictures1'
    bucket = storage_client.get_bucket(bucket_name)
    subscription_key = "1ce10fd9a4b142f9b31c020ec61d2393"
    assert subscription_key
    for source_file_name in source_file_names:
        blob = bucket.blob(os.path.basename("/pics/" + source_file_name))
        # Upload the local file to Cloud Storage.
        blob.upload_from_filename("/pics/" + source_file_name)
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
                cur.execute("SELECT * FROM users WHERE uid = " + index)
                row = cur.fetchone()
                tempPrivate += row[10]
                tempPrivate += url + " "
                cur.execute("UPDATE users SET private=%s WHERE uid = "+ index, (tempPrivate))
                con.commit()
            else:
                con = None
                con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
                cur = con.cursor()
                tempPublic = ""
                cur.execute("SELECT * FROM users WHERE uid = "+index)
                row = cur.fetchone()
                tempPublic += row[9]
                tempPublic += url + " "
                cur.execute("UPDATE users SET image=%s WHERE uid = " + index, (tempPublic))
                con.commit()
        except:
            print("damn")
        finally:
            if con:
                con.close()
    folder = 'pics/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def returnTopThree(index):
    con = None
    docs = []
    try:
        con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
        cur = con.cursor()
        qur = "SELECT * FROM users WHERE uid = " + str(index)
        cur.execute(qur)
        row = cur.fetchone()
        tempOrientation = row[7]
        print(tempOrientation)
        qur = "SELECT * FROM users"
        cur.execute(qur)
        while(True):
            row = cur.fetchone()
            if (row == None):
                break
            if(row[6] == tempOrientation):
                docs.append(row[11])
    except :
        if con:
            con.rollback()

        return -1
    finally:
        if con:
            con.close()
    tfidf = TfidfVectorizer().fit_transform(docs)
    cosine_similarities = linear_kernel(tfidf[index-1:index], tfidf).flatten()
    matches = sorted(range(len(cosine_similarities)), key=lambda i:cosine_similarities[i])[::-1][1:4]
    return matches

print(returnTopThree(5))







# def addAndUpdate(source_file_name, index):
#    url = addCloud(source_file_name)
#    subscription_key = "1ce10fd9a4b142f9b31c020ec61d2393"
#    assert subscription_key
#    vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
#    vision_analyze_url = vision_base_url + "analyze"
#    doc = ""
#    try:
#        headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
#        params   = {'visualFeatures': 'Tags'}
#        data     = {'url': URL}
#        response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
#        response.raise_for_status()
#        analysis = response.json()
#        for ele in analysis["tags"]:
#            intWeight = int(round(ele["confidence"]*10))
#            tag = ele["name"]+ " "
#            for i in range(intWeight):
#                doc += tag
#        if "person" in doc:
#            con = None
#            docs = []
#            con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
#            cur = con.cursor()
#            tempPrivate = ""
#            cur.execute("SELECT * FROM users WHERE Id=%s", (index))
#            row = cur.fetchone()
#            tempPrivate += row[10]
#            tempPrivate += url + " "
#            cur.execute("UPDATE users SET private=%s WHERE Id=%s", (tempPrivate, index))
#            con.commit()
#        else:
#            con = None
#            docs = []
#            con = psycopg2.connect("host='localhost' dbname='hackillinois2018'")
#            cur = con.cursor()
#            tempPublic = ""
#            cur.execute("SELECT * FROM users WHERE Id=%s", (index))
#            row = cur.fetchone()
#            tempPublic += row[9]
#            tempPublic += url + " "
#            cur.execute("UPDATE users SET image=%s WHERE Id=%s", (tempPublic, index))
#            con.commit()
#    except:
#        print("damn")
#    finally:
#        if con:
#            con.close()






#def createUserTags():


#INSERT INTO users(firstname, lastname, email, birthday, sex, orientation, location, address, pwdhash, image, private, tags, matched, flag, priv)
