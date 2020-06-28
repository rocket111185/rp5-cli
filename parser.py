#import urllib.request as req
from bs4 import BeautifulSoup as bs
import lxml.html as html

# url = input('URL for the forecast\n> ')
#url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A2%D0%B0%D1%83%D0%B6%D0%BD%D0%BE%D0%BC'

HOURS_COUNT = 0


#page = req.urlopen(url)
#data = html.document_fromstring(page.read())

file = open('weather.html').read()
data = html.fromstring(file)
soup = bs(file, 'html.parser')
tags = soup('td')
hours = []

record_mode = False
for tag in tags:
  if tag.get('colspan') == '2':
    contents = tag.text
    if len(contents) == 2:
      HOURS_COUNT += 1
      hours.append(contents)
      record_mode = True
    elif record_mode is True: break

print(hours)

temp = data.xpath('//div[@class="t_0"]//span[@class="otstup"]/following-sibling::text()')
temp = temp[:HOURS_COUNT]

rain_raw = data.xpath('//div[@class="pr_0"]//div')
rain = []
rain_ind = 0

for el in rain_raw:
  rain_inf = el.get('class')
  if not rain_inf.endswith('left'):
    rain_inf = rain_inf[-1]
    rain.append(rain_inf)
    rain_ind += 1
  if rain_ind is HOURS_COUNT:
    break

print(temp)
print(rain)
