import requests
import json

from config import white_key

street_line_1 = '5912 cactus valley'
city = 'Charlotte'
postal_code = '28277'
state_code='NC'
base_target_url = 'https://proapi.whitepages.com/3.0/location'

params = {
    'street_line_1': street_line_1,
    'city' : city,
    'postal_code': postal_code,
    'state_code':state_code,
    'api_key':white_key
}

response = requests.get(base_target_url,params)

print('response url is : ' + response.url)

data=  response.json()

print(json.dumps(data, indent=4, sort_keys=True))
