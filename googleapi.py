import requests
import pandas as pd
import time

# getting query from user
query = input("Input the query: ")

# setting up the request
key = open(".google_api").read()
url = "https://kgsearch.googleapis.com/v1/entities:search"
params = {
    "query": query,
    "limit": 10,
    "indent": True,
    "key": key,
}

# sending the request
result = requests.get(url, params=params)

# checking for weird google things where its just like nah i dont want to work
if not result.ok:
    print(result)
    print(result.text)

print(result.text)

# creating and formatting output
output = pd.json_normalize(result.json(), "itemListElement")
outputcsv = output[["result.name", "result.description", "resultScore", "result.detailedDescription.articleBody", "result.detailedDescription.url"]]

# save to googlesearch.csv
saved = False
while not saved:
    try:
        outputcsv.to_csv("googlesearch.csv")
    except PermissionError:
        print("Cannot save - is excel closed?")
        time.sleep(0.5)
    else:
        saved = True
        print("Saved")