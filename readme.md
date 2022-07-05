setting up the API:
go to https://developer.company-information.service.gov.uk/ and register an account<br>
create a new app on live environment<br>
go to view and find the app<br>
create a new REST key<br>
in the repository create a python file called “private.py” and put inside it “key = [your key here]”<br>
API has a ratelimit of 600 per 5 mins (0.5 per/sec)<br>

to change what is searched change the query variable in basicsearch.py<br>
the output will be saved into “search.csv” which can be opened in excel

The downside of this way is you need to know almost exactly the company name, which is not always easy

There is also a postcode search that will only show the companies that the postcode exactly, might not always be useful as if companies are not registered at the address

To search for the SIC codes, run the companysearch.py file. In the console, enter the company numbers, and enter a blank input to tell the program to start sending requests. I made the input system so that you can copy from the excel spreadsheet from the search program, and paste into the console.<br>

You can input unlimited company codes, but there a 0.5 second delay between each request to eliminate ratelimiting, as the way companies house api does ratelimiting is 600 requests per 5 minutes, which works out to 0.5 seconds per request to not have a few minutes of delay until it resets.<br>

The output is saved to companysearch.csv, with sic_codes in a list for each company.<br>