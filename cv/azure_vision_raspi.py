from picamera import PiCamera
from fractions import Fraction
import httplib, urllib, base64
import sys, subprocess, io
import json
from azure_keys import *

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': cognitive_services_key,
}

params = urllib.urlencode({
    # Request parameters
    'maxCandidates': '1',
})


def detect(image):
	try:
    		conn = httplib.HTTPSConnection('southcentralus.api.cognitive.microsoft.com')
    		conn.request("POST", "/vision/v1.0/describe?%s" % params, image.read(), headers)
    		response = conn.getresponse()
    		data = response.read()
    		conn.close()
                return data
	except Exception as e:
    		print("[Errno {0}] {1}".format(e.errno, e.strerror))

def speak(result):
    data = json.loads(result)
    caption = data["description"]["captions"][0]["text"] #.captions[0].text
    print caption
    subprocess.Popen(['./speech.sh', caption])

def capture():
    resolution = (640, 480)
    with PiCamera(
            resolution = resolution,
        ) as camera:
        stream = io.BytesIO()
        for frame in camera.capture_continuous(stream, "jpeg",quality=100):
            stream.seek(0)
            result = detect(stream)
            speak(result)
            stream.seek(0)
            stream.truncate()
            #enter for next photo
            line = raw_input("Press {enter} to capture again")

if __name__ == "__main__":
    capture()

