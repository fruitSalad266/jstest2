from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import json
# import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return({"message": "success"})

@app.get("/q")
def fetchQ(query: str):
    raw = requests.get('https://api.pullpush.io/reddit/search/submission/?q=' + query).text
    mapData = json.loads(raw)["data"]

    #add all this data 
    titleRaw = mapData[0]["title"]
    subreddit = "r/" + mapData[0]["subreddit"]
    link = 'https://reddit.com/' + mapData[0]["id"]

    print(subreddit)
    print("QUERY:", query)
    return({"title": titleRaw, "sr": subreddit, "link": link})

@app.get("/q2")
def fetchQ2(query: str):
    raw = requests.get('https://api.pullpush.io/reddit/search/submission/?q=' + query).text
    mapData = json.loads(raw)["data"]

    parsedData = [None] * len(mapData)
    #add all this data 
    print(len(mapData))
    for i, data in enumerate(mapData):
        title = data["title"]
        sr = "r/" + data["subreddit"] 
        url = 'https://reddit.com/' + data["id"]
        nsfw = data["thumbnail"] == "nsfw"
        
        parsedData[i] = ({"title": title, "sr":  sr, "link": url, "nsfw": nsfw})

    return(parsedData)

if __name__ == "__main__":
    uvicorn.run("server:app", port=8000, reload=True)