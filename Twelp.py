#This code is a proof of concept for Project 1 of EC601 at Boston University
#It is "Twelp" a twitter based yelp like program that will search the recent tweets based
#on a restaurant name.
#Used this website as a guide https://towardsdatascience.com/an-extensive-guide-to-collecting-tweets-from-twitter-api-v2-for-academic-research-using-python-3-518fcb71df2a

#For sending GET requests from the API
import requests
#For saving access tokens and for file management when creating and adding to the dataset
import os
from dotenv import load_dotenv
#For dealing with json responses we receive from the API
import json

#load the bearer_token from the dotenv file
load_dotenv()
def auth():
    return os.getenv("BEARER_TOKEN")

#create a header to use in the GET request
def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format((bearer_token))}
    return headers

#create the url
def create_url(keyword, max_results = 10):

    search_url = "https://api.twitter.com/2/tweets/search/recent"
    #The query parameters that will be pulled
    query_params = {'query': keyword,
                    'max_results': max_results,
                    'expansions': 'geo.place_id',
                    'tweet.fields': 'id,text,author_id,geo,created_at,lang',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)

#The function that will make the request
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))

    #reports the error code if there was any
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#Inputs for the request
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = input("Enter a name of a restaurant: ")
query = keyword +" lang:en -is:retweet"
max_results = 100

url = create_url(query, max_results)

json_response = connect_to_endpoint(url[0], headers, url[1])

with open('data.json', 'w') as f:
    json.dump(json_response, f)


