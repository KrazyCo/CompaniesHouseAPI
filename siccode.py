import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class Siccodes:
    def __init__(self):
        self.url = "https://siccode.com/search-business/{}"

    def search(self, query):
        query = query.replace(" ", "+") # replace spaces with +
        url = self.url.format(query) # putting in search query

        # sending request
        result = requests.get(url)

        # if result code >= 399 (i.e. something went wrong)
        if not result.ok:
            print(result)
            print(result.text)
            return

        # setting up soup data structure
        soup = BeautifulSoup(result.text, "html.parser")
        # finding each ul element in section results (page is split up because of ads)
        uls = soup.find("section", {"id":"results"}).find_all("ul")
        lis = []
        # iterating through each li element
        for ul in uls:
            for li in ul.find_all("li"): # this is dumb
                lis.append(li) 

        results = []
        # iterating through each listElement in lis to find name, naics and other stuff
        for listElement in lis:
            name = listElement.find("div").text
            naics = listElement.find("div", {"class":"description"}).find("span").text
            naicsDescription = listElement.find("div", {"class":"description"}).text[len(naics)+4:].strip()
            location = listElement.find("div", {"class":"country"}).find("span").text
            # append dictionary to list
            results.append({"name":name, "naics":naics, "naicsDescription":naicsDescription, "location":location})

        # return list of dictionarys
        return results

# if program isnt imported
if __name__ == "__main__":
    siccodes = Siccodes()
    lookup = siccodes.search("FM Global")
    output = pd.json_normalize(lookup)

    # save to siccodes.csv
    saved = False
    while not saved:
        try:
            output.to_csv("siccodes.csv")
        except PermissionError:
            print("Cannot save - is excel closed?")
            time.sleep(0.5)
        else:
            saved = True
            print("Saved")