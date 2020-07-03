# rp5-cli

The CLI client for RP5 weather forecasting site.

## Requirements

* `python3`, of course
* `bs4` (BeautifulSoup)
* `lxml`
* `tabulate`
* `google`

Installation script will resolve it itself.

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
+----------------------+
|        Monday        |
|----------------------|
| 03:00 | 21°C | 0' mm |
| 09:00 | 27°C | 0' mm |
| 15:00 | 32°C | 1' mm |
| 21:00 | 29°C | 1' mm |
+----------------------+
```

Also you can type like this:
```bash
$ rp5-cli Cairo
# ...
# Some results for Cairo...
# ...
$ rp5-cli The capital of Great Britain
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
