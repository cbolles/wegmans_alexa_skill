from models.request import AlexaResponse
import requests

def lambda_handler(event, context):
    intent = event['request']['intent']['name']
    message = ''
    if intent == 'Add_to_List':
        request_url = 'https://brickhackv-232001.appspot.com/add_item?item_keyword='
        food_keyword = event['request']['intent']['slots']['name']['value']
        requests.get(request_url + food_keyword)
        message = 'Added ' + food_keyword + ' to list'
    if intent == 'Output_List':
        request_url = 'https://brickhackv-232001.appspot.com/get_list'
        r = requests.get(request_url)
        food_list = ''
        for item in r.json():
            food_list += item['product_name'] + ', '
        message = 'You have ' + food_list + 'in your list'
    alexa_response = AlexaResponse("Tile", message)
    return alexa_response.get_statement()