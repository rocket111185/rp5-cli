from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import lxml.html as html
from tabulate import tabulate
import time

# Request for the URL
url = input('URL for the forecast\n> ')
# You can just press the Enter key.
# The result is site of weather in Tauzhne forecast
if len(url) < 1:
  url = 'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A2%D0%B0%D1%83%D0%B6%D0%BD%D0%BE%D0%BC'

# Read the contents of the page
page = urlopen(url).read()
# For LXML parsing
data = html.document_fromstring(page)
# For BeautifulSoup parsing
soup = bs(page, 'html.parser')
tags = soup('td')

# Initial names of the week
week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Calculate the position of name of the 
# today's name in the `week` array
day_is_today = time.strftime('%A')
day_number = week.index(day_is_today)
# Constant, that keeps the number of days in the week.
# It's clear the number is 7, but... less magic in code)
NUMBER_OF_DAYS_IN_WEEK = len(week)

# Read the hours on the site (6-days variant)
hours = []
# The problem is:
# soup with <td> tags keeps trash values (mark them as @)
# and needed hour values in the same place:
# [@, @, @, '03', '09', ..., '21', @, ..., @]
# Hopefully, hour values are placed in the row, so
# we can determine the start of these values and
# copy them till they are run out of.
record_mode = False
for tag in tags:
  # Tags with hour values have attribute
  # 'colspan' with the value '2'
  if tag.get('colspan') == '2':
    contents = tag.text
    # Only the hour values have the length of 2
    if len(contents) == 2:
      # Transform 'HH' into readable 'HH:00'
      hours.append(contents + ':00')
      record_mode = True
    elif record_mode is True: break

# Number of hours for the 6-day table variant
HOURS_COUNT = len(hours)

# Get the temperature values with this scheme.
# Authors of the RP5 site, burn in hell!
temp = data.xpath('//div[@class="t_0"]//span[@class="otstup"]/following-sibling::text()')
# Only the first HOURS_COUNT values are needed
# (they are from 6-day table)
temp = temp[:HOURS_COUNT]
# It's time to beautify the values
for i in range(len(temp)):
  curr_temp = temp[i]
  # If the value is one-digit, the row becomes
  # ugly (most of values are two-digit).
  # In this case, just put a space at the
  # beginning of the string.
  if len(curr_temp) < 2:
    curr_temp = ' ' + curr_temp
  # Add fancy degree sign
  temp[i] = curr_temp + '°C'

# Get the precipitation tags with this scheme.
# Authors of the RP5 site, burn in hell, twice! 
rain_raw = data.xpath('//div[@class="pr_0"]//div')
# This array will contain values, prepared for
# the output.
rain = []
# Count the precipitation values (there are must
# be HOURS_COUNT of them)
rain_count = 0

# The value of the precipitation is in tag
# attribute 'class' value.
for tag in rain_raw:
  rain_inf = tag.get('class')
  # The smth_left values are not informative.
  if not rain_inf.endswith('left'):
    # The last symbol is the needed 
    # precipitation value.
    rain_inf = rain_inf[-1]
    # Make the value fancy, again
    # NOTE: ' sign means nothing.
    # It's just a way to make table
    # symmetric.
    rain.append(rain_inf + '\' mm')
    rain_count += 1
  if rain_count is HOURS_COUNT:
    break

# For the late time (now is 22:13, but
# the next forecast is for 03:00, tomorrow)
# situation is ok.
# But when the forecast for today is available,
# it becomed signed as tomorrow day.
current_hour = time.strftime('%A')
if hours[0] < current_hour:
  day_number -= 1

# The assosiative table (key - day, value -
# - array of rows of contents)
tables = dict()
current_hour = hours[0]
for i in range(len(hours)):
  # Find when the next day starts (for the first
  # day detection, the problem is described above)
  if hours[i] <= current_hour:
    day_number += 1
    # When we jump from Sunday to Monday, the day
    # number (index) becomes overflowed.
    if day_number is NUMBER_OF_DAYS_IN_WEEK:
      day_number = 0
    # Assosiate the blank array with the day's name
    day_name = week[day_number]
    tables[day_name] = []
  # Write the row to the array
  tables[day_name].append(hours[i] + ' | ' + temp[i] + ' | ' + rain[i])
  # It would be right to call it `previous_hour`...
  current_hour = hours[i]

# Print out the tables with the forecast
for key in tables:
  table = dict()
  table[key] = tables[key]
  print(tabulate(table, headers=table.keys(), tablefmt='psql', stralign='center') + '\n')

