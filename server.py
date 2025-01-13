from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
import json
# import random

description = """
JSTEST2 API helps me do awesome stuff (fetch pushpull api). 🚀
It also helps you because you can do the awesome stuff too. ️‍🔥

## Items

You can **read [reddit] submissions**.

## Users

You will be able to:

* **Be successful (probably)**.
* **Preview 1 (one) Reddit post**.
* **Preview multiple (up to one hundred (100)) Reddit posts**.
"""

tags_metadata = [
    {
        "name": "Query: single",
        "description": "Fetches a single reddit submission",
    },
    {
        "name": "Query: multiple",
        "description": "Fetches multiple reddit submissions",
    },
]

app = FastAPI(
    title="JSTEST2",
    description=description,
    version="0.0.3",
    contact={
        "name": "Matt N",
        "email": "mattcng9 at uw",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
    )

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

@app.get("/q", tags=["Query: single"])
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

@app.get("/q2", tags=["Query: multiple"])
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

#Uncomment if running locally
# if __name__ == "__main__":
#     uvicorn.run("server:app", port=8000, reload=True)