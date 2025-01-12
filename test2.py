from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

query = "cookie"
raw = requests.get('https://api.pullpush.io/reddit/search/submission/?q=' + query).text
mapData = json.loads(raw)["data"]

parsedData = [None] * len(mapData)
#add all this data 
print(len(mapData))
for i, data in enumerate(mapData):
    title = data["title"]
    sr = "r/" + data["subreddit"] 
    url = 'https://reddit.com/' + data["id"]
    
    parsedData[i] = "{title:" + title + "sr: " + sr + "url: " + url + "}"

print(parsedData)