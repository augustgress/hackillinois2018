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

#image_caption = analysis["description"]["captions"][0]["text"].capitalize()
#print(image_caption)

print(analysis["tags"])









# import http.client, urllib.request, urllib.parse, urllib.error, base64
#
# headers = {
#     # Request headers
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': 'bcc31143253f412a80d0e8ec15938001',
# }
#
# params = urllib.parse.urlencode({
# })
#
# try:
#     conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
#     conn.request("POST", "/vision/v1.0/tag?%s" % params, "{body}", headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))
