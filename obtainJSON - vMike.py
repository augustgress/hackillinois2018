import requests

subscription_key = "bcc31143253f412a80d0e8ec15938001"
assert subscription_key

vision_base_url = "https://eastus.api.cognitive.microsoft.com/vision/v1.0/"
vision_analyze_url = vision_base_url + "analyze"

image_url = "https://assets.capitalxtra.com/2017/49/lil-pump-instagram-2-1512392221-view-1.png"


headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Tags'}
data     = {'url': image_url}
response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
response.raise_for_status()
analysis = response.json()

#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
#print(image_caption)

#print(analysis["tags"][0]["confidence"])

def AccountDocTag(URL):
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
    params   = {'visualFeatures': 'Tags'}
    data     = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    response.raise_for_status()
    analysis = response.json()
    doc = ""
    for ele in analysis["tags"]:
        intWeight = int(round(ele["confidence"]*10))
        tag = ele["name"]+ " "
        for i in range(intWeight):
            doc += tag
    print(doc)


AccountDocTag(image_url)
