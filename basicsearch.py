import time
from private import key
import requests
import pandas as pd

url = "https://api.companieshouse.gov.uk/search/companies?items_per_page=100&q={}"

query = "tesco"

query = query.replace(" ","+")
query = query.replace("&","%26")

result = requests.get(url.format(query), auth=(str(key),''))

# print(result.json())
# print(f"{result.json()['total_results'] = }")

output = pd.json_normalize(result.json(), "items")
# print(output)
outputcsv = output[["title", "company_number", "company_status", "description", "address_snippet", "company_type", "address.postal_code"]]
# print(outputcsv)

saved = False
while not saved:
    try:
        outputcsv.to_csv("search.csv")
    except PermissionError:
        print("Cannot save - is excel closed?")
        time.sleep(0.5)
    else:
        saved = True
        print("Saved")