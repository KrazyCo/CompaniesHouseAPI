import time
from private import key
import requests
import pandas as pd
from datetime import datetime

url = "https://api.companieshouse.gov.uk/company/{}"

# getting list of company numbers
queryList = []
end = False
while not end:
    userInput = input("Enter company names, blank input to continue: ")
    if userInput != "":
        userInput = (8-len(userInput))*"0"+userInput
        queryList.append(userInput)
    else:
        end = True

# sending requests for each company 
results = []
lastTime = datetime.now()
for value in queryList:
    currentTime = datetime.now()

    result = requests.get(url.format(value), auth=(str(key),''))
    print(result.json()["company_name"])
    results.append(result.json())

    # ratelimiting
    timeSinceRequest = (currentTime-lastTime).total_seconds()
    timeToWait = max(0.5 - timeSinceRequest, 0)
    time.sleep(timeToWait)
    lastTime = datetime.now()

# formatting output
output = pd.json_normalize(results)
outputcsv = output[["company_name", "company_number", "sic_codes", "company_status", "date_of_creation", "company_status", "registered_office_address.address_line_1", "registered_office_address.address_line_2", "registered_office_address.region", "registered_office_address.locality", "registered_office_address.postal_code"]]

# save to companysearch.csv
saved = False
while not saved:
    try:
        outputcsv.to_csv("companysearch.csv")
    except PermissionError:
        print("Cannot save - is excel closed?")
        time.sleep(0.5)
    else:
        saved = True
        print("Saved")