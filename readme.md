setting up the API:
go to https://developer.company-information.service.gov.uk/ and register an account
create a new app on live environment
go to view and find the app
create a new REST key
in the repository create a python file called “private.py” and put inside it “key = [your key here]”
API has a ratelimit of 600 per 5 mins (0.5 per/sec)

to change what is searched change the query variable in basicsearch.py
the output will be saved into “search.csv” which can be opened in excel

The downside of this way is you need to know almost exactly the company name, which is not always easy

There is also a postcode search that will only show the companies that the postcode exactly, might not always be useful as if companies are not registered at the address
