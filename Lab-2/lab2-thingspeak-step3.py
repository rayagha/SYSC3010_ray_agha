import json
import requests

def reaData_thinkSpeak():
    URL = 'https://api.thingspeak.com/channels/1152847/feeds.json?api_key='
    KEY = '2NRMMU5S7ZVIE0JD'
    HEADER = '&result=4'
    nURL = URL+KEY+HEADER
    print (nURL)
    
    getData = requests.get(nURL).json()
    print (getData)
    channeId = getData['channel']['id']
    
    feed1 = getData['feeds']
    
    fi = []
    for x in feed1:
        fi.append(x['entry_id'])
        print (fi)
reaData_thinkSpeak()
 