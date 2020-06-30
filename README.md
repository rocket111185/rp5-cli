# rp5-cli

The CLI client for RP5 weather forecasting site.

## Requirements

* `python3`, of course
* `bs4` (BeautifulSoup)
* `lxml`
* `tabulate`

You can resolve the dependencies with one command:
```bash
$ pip3 install bs4 lxml tabulate
```

## Usage
To launch the program, type:
```bash
$ python3 parser.py
```
The program will prompt you for the city name, and
then it will search for the proper URL, parse...

The output is a set of named tables (name is day of the week) with
rows in format `TIME | TEMPERATURE | PRECIPITATION`.

For example (one of the days):
```
+---------------------+
| Friday              |
|---------------------|
| 02:00 | 24°C | 0 mm |
| 08:00 | 23°C | 0 mm |
| 14:00 | 36°C | 0 mm |
| 20:00 | 34°C | 0 mm |
+---------------------+
```

### Contributors
Rekechynsky Dmytro, D_MENT
