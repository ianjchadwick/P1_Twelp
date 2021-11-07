import pytest
from Twelp import *

#Initialize some variables for tests
#You must have your own Twitter API Bearer Token saved in dotenv and a services.json file from the Google NLP API in the
#same directory see https://cloud.google.com/docs/authentication/production#windows for details on how to get your services.json
load_dotenv()
bearer_token_test_var = os.getenv("BEARER_TOKEN")
keyword_test = 'Burger King'
max_results_test = 100

#this is a modified verson of the Google NLP API funciton without the print statements because I was having trouble
#making unit tests to compare print statements. This is the same function, minus the print statements. It instead outputs
#the total document score.
def NLP_analyze_sentiment(text_content):
    """
    Analyzing Sentiment in a String

    Args:
      text_content The text content to analyze
    """

    client = language_v1.LanguageServiceClient.from_service_account_json('services.json')

    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    return response.document_sentiment.score

@pytest.mark.basic_functionality
def test_auth():
    test = auth()
    assert test == bearer_token_test_var

def test_create_headers():
    header_test = create_headers(bearer_token_test_var)
    expected_out = "Bearer {}".format(bearer_token_test_var)
    assert header_test.get('Authorization') == expected_out

def test_create_url():
    output = create_url(keyword_test, max_results_test)
    assert output[1].get('query') == keyword_test
    assert output[1].get('max_results') == max_results_test

#the each time this is run, the results will be different because it is getting live data from Twitter, so in order to
#test to see if the request to the API is working it should return a json dict so we can test to see if the output is a dict
def test_twitter_api():
    test_url = create_url(keyword_test, max_results_test)
    headers = create_headers(bearer_token_test_var)
    test_output = connect_to_endpoint(test_url[0],headers,test_url[1])
    assert type(test_output) == dict

#extracts the text from test.json which is included in the directory.
def test_extract_text():
    test_text = extract_tweet_text.extract_tweet_text('test.json')
    assert test_text == " Burger King test tweet. Burger King test tweet sentence 2."

#I ran the test string below in advance to get the total document score in order to compare it to the ouput of the
#modified NLP function above
def test_google_nlp_api():
    nlp_output = NLP_analyze_sentiment("Hooray! This is the BEST test ever! I am so happy")
    assert nlp_output == 0.800000011920929
