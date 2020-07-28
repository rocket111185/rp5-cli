from urllib.parse import urlparse, unquote
from urllib.error import HTTPError
from googlesearch import search
from rp5_parser import print_weather

# Initialize variable `city_name`
city_name = ''

try:
    # Request for the city name
    city_name = input('''Welcome to RP5-CLI!
It's easy-to-use RP5 forecast service client.
All you need, is to input the name of desired city.\n> ''')
except (EOFError, KeyboardInterrupt):
    print()
    exit(0)

# The default city is Tauzhne
if len(city_name) < 1:
    city_name = 'Tauzhne'

# Make a query for Google
query = 'rp5 ' + city_name
# You can control number of attempts, changing the `stop` value
urls = search(query, tld='com', lang='ua', start=0, stop=10)

# The default value for `url`
url = None
# If it could reach the site, the `visited`
# becomes true.
visited = False

# Go through pages.
for link in urls:
    url = link
    # Show the name of web page to see
    # that Google returned correct link.
    print(unquote(urlparse(link).path))
    # All the details in rp5_parser.py
    try:
        print_weather(url)
        visited = True
        break
    except (IndexError, HTTPError):
        print('Wrong page.')

if not visited:
    print('Unfortunately, it couldn\'t reach the needed cite.')
