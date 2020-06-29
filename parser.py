from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import lxml.html as html
from tabulate import tabulate
import time

url = input('URL for the forecast\n> ')
if len(url) < 1:
  url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A2%D0%B0%D1%83%D0%B6%D0%BD%D0%BE%D0%BC'

page = urlopen(url).read()
data = html.document_fromstring(page)

#file = open('weather.html').read()
#data = html.fromstring(file)

soup = bs(page, 'html.parser')
tags = soup('td')
hours = []

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_is_today = time.strftime('%A')
day_number = week.index(day_is_today)
current_hour = time.strftime('%A')
NUMBER_OF_DAYS_IN_WEEK = len(week)

record_mode = False
for tag in tags:
  if tag.get('colspan') == '2':
    contents = tag.text
    if len(contents) == 2:
      hours.append(contents + ':00')
      record_mode = True
    elif record_mode is True: break

HOURS_COUNT = len(hours)
if hours[0] < current_hour:
  day_number -= 1

temp = data.xpath('//div[@class="t_0"]//span[@class="otstup"]/following-sibling::text()')
temp = temp[:HOURS_COUNT]
for i in range(len(temp)):
  curr_temp = temp[i]
  if len(curr_temp) < 2:
    curr_temp = ' ' + curr_temp
  temp[i] = curr_temp + '°C'

rain_raw = data.xpath('//div[@class="pr_0"]//div')
rain = []
rain_ind = 0

for el in rain_raw:
  rain_inf = el.get('class')
  if not rain_inf.endswith('left'):
    rain_inf = rain_inf[-1]
    rain.append(rain_inf + ' mm')
    rain_ind += 1
  if rain_ind is HOURS_COUNT:
    break

table = dict()
current_hour = hours[0]
for i in range(len(hours)):
  if hours[i] <= current_hour:
    day_number += 1
    if day_number is NUMBER_OF_DAYS_IN_WEEK:
      day_number = 0
    day_name = week[day_number]
    table[day_name] = []
  table[day_name].append(hours[i] + ' | ' + temp[i] + ' | ' + rain[i])
  current_hour = hours[i]

for key in table:
  temp_dict  = dict()
  temp_dict[key] = table[key]
  print(tabulate(temp_dict, headers=temp_dict.keys(), tablefmt='psql') + '\n')
