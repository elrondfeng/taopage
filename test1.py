import urllib2
import urllib
# Specify the url
url = 'https://proapi.whitepages.com/3.0/location?api_key=7277d73b4f0542769bb79eb1ab25c676&city=Charlotte&country_code=USA&postal_code=28277&state_code=NC&street_line_1=5916+Cactus+Valley+Rd'
# Package Request
request = urllib2.Request(url)
# Send the request and retrieve the response
response = urllib2.urlopen(request)
# Extract the response
html = response.read()
# Display response
print html