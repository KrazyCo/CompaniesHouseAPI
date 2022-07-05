import time
from private import key
import requests
import pandas as pd

# postcode goes here
query = "SL6 2PJ"

# api url
url = "https://api.companieshouse.gov.uk/search/companies?items_per_page=20&q={}"

# replacing space and &, and saving a clean copy to querypostcode for later
querypostcode = query
query = query.replace(" ","+")
query = query.replace("&","%26")

# get request using url with query inside, and api key
result = requests.get(url.format(query), auth=(str(key),''))

# find all items that do not fit postcode
output = result.json()["items"]
toRemove = []
for i in range(0, len(output)):
    if not output[i]["address"]["postal_code"].upper() == querypostcode.upper():
        toRemove.append(i)

# remove all items that do not fit postcode
for i in range(len(toRemove)):
    output.pop(toRemove[i]-i)

# find all items that are dissolved
toRemove = []
for i in range(0, len(output)):
    if output[i]["company_status"].upper() == "DISSOLVED":
        toRemove.append(i)

# remove all items that are dissolved
for i in range(len(toRemove)):
    output.pop(toRemove[i]-i)

# making the output normalised thing
output = pd.json_normalize(output)
outputcsv = output[["title", "company_number", "company_status", "description", "address_snippet", "company_type", "address.postal_code"]]

# save to csv with checking to see if its writable (excel locks it)
saved = False
while not saved:
    try:
        outputcsv.to_csv("postcodesearch.csv")
    except PermissionError:
        print("Cannot save - is excel closed?")
        time.sleep(0.5)
    else:
        saved = True
        print("Saved")