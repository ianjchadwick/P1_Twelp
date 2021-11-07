# "TWELP" (Twitter based Yelp)
Using Twitter API V2 to search tweets for restaurant names and feed the first 100 most recent matches to Google Natural Language Processing API to determine the sentiment of the tweets about that restaurant.

The application will ask the user for a name of a restaurant and then it will use that as a search query into the Twitter APIv2 to get the most recent 100 results. Then it will take those results and feed them to the Google Natural Language Processing API to determine the sentiment of the tweets about that restaurant. The application will give a sentiment score and a magnitude for all of the tweets overall and will also list out a breakdown of the tweets sentence by sentence. So, if desired, the user can look through the tweets and their associated scores and magnitudes to help inform their decision of whether or not to eat there.

## User Stories

I as a potential patron of a restaurant want to know if this particular restaurant has been talked about on twitter and if so, whether people have been saying good or bad things about it.

I as a potential patron of a restaurant want to know whether people were talking about the food, the service or something else about the restaurant.

##  How-To:

Requires Twitter Bearer-Token be in a .env file in the environment saved as "BEARER_TOKEN" and google NLP service.json saved in the same directory with the API access keys in it to access the appropriate APIs. See https://cloud.google.com/docs/authentication/production#windows for information on how to create a services.json file.

Then simply run Twelp.py, enter in the name of a restaurant and the results will appear in the console as well as be exported to data.json in the directory. 

## Unit Tests:

The way I originally wrote this program was not really that "unit test friendly", since for every run, the results will be different. So, I have written unit tests for each of the functions that are called. The google NLP function was modified to return the document's sentiment score so that it could be compared to the sentiment of a fixed string with a known sentiment value to ensure that it was working as intended.

Functions tested
* auth
* create_headers
* create_url
* connect_to_endpoint
* extract_text
* sample_analyze_sentiment
