import json

subscription_key = "bcc31143253f412a80d0e8ec15938001"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"

image_url = "https://i.pinimg.com/564x/ba/25/fa/ba25fa54446b057b5adb5cd26e4a6181--zero-playing-cards.jpg"

import requests
headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Tags'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

allresults = (analysis["tags"])
nameList = []
confidList = []

#storing all of the names in an array
for i in allresults:
    nameList.append(i['name'])
    confidList.append(int(round(i['confidence']*10)))
    
    
print(nameList[1])
print(confidList[1])
    

