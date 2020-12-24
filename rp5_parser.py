def print_weather(url):
    global day_name
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import lxml.html as html
    from tabulate import tabulate
    import time

    # Read the contents of the page
    page = urlopen(url).read()
    # For LXML parsing
    data = html.document_fromstring(page)
    # For BeautifulSoup parsing
    soup = BeautifulSoup(page, 'html.parser')
    tags = soup('td')

    # Initial names of the week
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # Calculate the position of name of the
    # today's name in the `week` array
    day_is_today = time.strftime('%A')
    day_number = week.index(day_is_today)
    # Constant, that keeps the number of days in the week.
    # It's clear the number is 7, but... less magic in code)
    number_of_days_in_week = len(week)

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
                hours.append(contents)
                record_mode = True
            elif record_mode is True:
                break

    # Number of hours for the 6-day table variant
    hours_count = len(hours)

    # Get the temperature values with this scheme.
    # Authors of the RP5 site, burn in hell!
    temp_raw = data.xpath('//div[@class="t_0"]//b/text()')
    # This array will contain values, prepared for
    # the output.
    temp = []
    # Only the first hours_count values are needed
    # (they are from 6-day table)
    temp_count = 0

    # Add needed values to the `rain` from `rain_raw`
    for t in temp_raw:
        # Positive values of temperature are '+' and exact value,
        # dividen by <span> tag.
        # So, we can just ignore '+' signs and go ahead.
        if t != '+':
            # There are can be '-TT' values of temperature,
            # that's why it's useful to add spaces.
            while len(t) < 3:
                t = ' ' + t
            temp.append(t)
            temp_count += 1
        if temp_count is hours_count: break


    # Get the precipitation tags with this scheme.
    # Authors of the RP5 site, burn in hell, twice!
    rain_raw = data.xpath('//div[@class="pr_0"]//div')
    # This array will contain values, prepared for
    # the output.
    rain = []
    # Count the precipitation values (there are must
    # be hours_count of them)
    rain_count = 0

    # The value of the precipitation is in tag
    # attribute 'class' value.
    for tag in rain_raw:
        rain_inf = tag.get('class')
        # The smth_left values are not informative.
        if not rain_inf.endswith('left'):
            # Find the symbol which is the needed
            # precipitation value.
            rain_last_ind = 0
            while True:
              rain_last_ind = rain_last_ind + 1
              rain_val = rain_inf[-rain_last_ind]
              if rain_val.isnumeric(): break
            # Make the value fancy, again
            # NOTE: . sign means nothing.
            # It's just a way to make table
            # symmetric.
            rain.append(rain_val + '. mm')
            rain_count += 1
        if rain_count is hours_count:
            break

    # For the late time (now is 22:13, but
    # the next forecast is for 03:00, tomorrow)
    # situation is ok.
    # But when the forecast for today is available,
    # it becomes signed as tomorrow day.
    current_hour = time.strftime('%H')
    if hours[0] > current_hour:
        day_number -= 1

    # The associative table (key - day, value -
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
            if day_number is number_of_days_in_week:
                day_number = 0
            # Assosiate the blank array with the day's name
            day_name = week[day_number]
            tables[day_name] = []
        # Write the row to the array
        tables[day_name].append(hours[i] + ':00 |' + temp[i] + '°C | ' + rain[i])
        # It would be right to call it `previous_hour`...
        current_hour = hours[i]

    # Print out the tables with the forecast
    for key in tables:
        table = dict()
        table[key] = tables[key]
        print(tabulate(table, headers=table.keys(), tablefmt='psql', stralign='center') + '\n')
