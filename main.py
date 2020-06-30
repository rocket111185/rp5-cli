from urllib.parse import urlparse, unquote
from googlesearch import search
from rp5_parser import print_weather

try:
  # Request for the city name
  city_name = input('''Welcome to RP5-CLI!
It's easy-to-use RP5 forecast service client.
All you need, is to input the name of desired city.\n> ''')
except:
  print()
  exit(0)

# The default city is Tauzhne
if len(city_name) < 1:
  city_name = 'Tauzhne'

# Make a query for Google
query = 'rp5 ' + city_name
urls = search(query, tld='com', lang='ua', start=0, stop=1)

# `urls` is the iterable object, so
# we need to do some iteration.
for link in urls:
  url = link
  # Show the name of webpage to see
  # that Google returned correct link.
  print(unquote(urlparse(link).path))

# All the details in rp5_parser.py
try:
  print_weather(url)
except:
  print('''It is possible that the incorrect name of city was written.
Try another.''')