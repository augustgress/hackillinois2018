import os

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
