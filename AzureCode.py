subscription_key = "0ac91a2a67054c9d97a44db7a70d61d6"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "analyze"
image_url = "https://storage.googleapis.com/userpictures1/hike.jpg"

import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Tags, Categories'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(analysis)


//INSERT INTO users(firstname, lastname, email, birthday, sex, orientation, location, address, pwdhash, image, private, tags, matched, flag, priv)
