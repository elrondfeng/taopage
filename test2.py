from whitepages import WhitePages

key = '7277d73b4f0542769bb79eb1ab25c676'

w = WhitePages(key)

location_result = w.location(street_line_1="5916 Cactus Valley Rd",city="Charlotte", state_code="NC")
