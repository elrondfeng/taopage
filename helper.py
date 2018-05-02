import json
import urllib
import urllib2

from error import WhitePagesError


def validate_url(result):
    if 'error' in result.keys():
        error_detail = result['error']
        raise WhitePagesError, error_detail


def url_encoder(params):
    encoded_params = urllib.urlencode(params)
    return encoded_params


def return_json(url):
    result_dict = json.load(urllib.urlopen(url))
    return result_dict


def dictIsEmpty(input_dict):
    return not bool(input_dict)


def remove_blank_fields(input_dict):
    return dict((k, v) for k, v in input_dict.iteritems() if v is not None)


def add_key(white_pages_object, request_dict):
    request_dict['api_key'] = white_pages_object.api_key
    return request_dict


def query(white_pages_object, request_object):

    url = request_object.url()

    input_dict = remove_blank_fields(request_object.to_dict())

    if dictIsEmpty(input_dict):
        error_detail = 'You have not entered any valid arguments'
        raise WhitePagesError, error_detail

    input_dict = add_key(white_pages_object, input_dict)

    url_query = url + url_encoder(input_dict)

    print("the url used is : " + url_query)

    results = json.load(urllib.urlopen(url_query))

    print 'results 1 : '
    print(results['is_valid'])

##############################################################

    request = urllib2.Request(url_query)
    # Send the request and retrieve the response
    response = urllib2.urlopen(request)
    # Extract the response
    html = response.read()
    # Display response
    print 'html : '
    print html

##############################################################