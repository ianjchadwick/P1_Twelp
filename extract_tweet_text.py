import json

#Takes a tweet json file and extracts the text from it into one long string
def extract_tweet_text(filename):
    with open(filename, 'r') as file:
        jsonData = json.load(file)
    text = ''
    for tweet in jsonData["data"]:
        text = text + " " + tweet.get('text')
    return text
