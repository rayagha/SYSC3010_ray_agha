import requests
import urllib.request
import json


URL = 'https://api.thingspeak.com/update?api_key='
KEY = '54CDA6FJF4RCJ92C'
HEADER = '&field1={ray.agha@carleton.ca}&field2={L2-M-11}&field3={a}'
NEWURL = URL+KEY+HEADER
print(NEWURL)

data = urllib.request.urlopen(NEWURL)
print(data)

    