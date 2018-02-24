subscription_key = "0ac91a2a67054c9d97a44db7a70d61d6"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"

vision_analyze_url = vision_base_url + "analyze"
image_url = "http://img1.sunset.timeinc.net/sites/default/files/styles/4_3_horizontal_-_1200x900/public/image/2016/09/main/camping-with-kids-lake-alpine-sierra-nevada-family-night-out-0514.jpg?itok=ocbTWgVV"

import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Tags, Categories'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
print(analysis)
