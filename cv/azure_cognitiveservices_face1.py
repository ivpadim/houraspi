import cognitive_face as CF
from azure_keys import *


CF.Key.set(face_api_key)
CF.BaseUrl.set(face_api_url)

photo_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'

print('Detecting face')

result = CF.face.detect(photo_url)

print result

