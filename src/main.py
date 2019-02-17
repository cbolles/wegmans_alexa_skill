from models.request import AlexaResponse
import requests

def lambda_handler(event, context):
    intent = event['request']['intent']['name']
    requests_url = 'https://brickhackv-232001.appspot.com/add_item?item_keyword='
    message = ''
    if intent == 'Add_to_List':
        food_keyword = event['request']['intent']['slots']['name']['value']
        requests.get(requests_url + food_keyword)
        message = 'Added ' + food_keyword + ' to list'
    alexa_response = AlexaResponse("Tile", message)
    return alexa_response.get_statement()