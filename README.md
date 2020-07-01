# rp5-cli

The CLI client for RP5 weather forecasting site.

## Requirements

* `python3`, of course
* `bs4` (BeautifulSoup)
* `lxml`
* `tabulate`
* `google`

You can resolve the dependencies with one command:
```bash
$ pip3 install bs4 lxml tabulate
```

## Installation

Easy, as pie.
```bash
$ ./install.sh
```

## Uninstallation
```bash
$ ./uninstall.sh
````
That's it!

## Usage
After the installation, type:
```bash
$ rp5-cli
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

Also you can type like this:
```bash
$ rp5-cli Cairo
# ...
# Some results for Cairo...
# ...
$ rp5-cli 'The capital of Great Britain'
# ...
# Some results for London (OMG)...
# ...
```
But the prompt will appear, again.
In this case, don't pay any attention, just wait.

If the name of city isn't in RP5 database, an error will occur.
So you must try type another name of city.

I hope you'll find this application useful.

### Contributors
Rekechynsky Dmytro, D_MENT
