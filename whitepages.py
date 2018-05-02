from helper import query
from location import LocationRequest

class WhitePages():
    def __init__(self, api_key):
        self.api_key = api_key

    def location(self, street_line_1=None, street_line_2=None, city=None, postal_code=None, state_code=None,
                 country_code=None, lat=None, lon=None, radius=None):
        return query(self, LocationRequest(street_line_1, street_line_2, city, postal_code, state_code,
                                           country_code, lat, lon, radius))