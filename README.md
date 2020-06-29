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
It will prompt for the URL.

This program has parser only for rp5.ru, that is why URL should
start from `'https://rp5.ru/'`.

### Contributors
Rekechynsky Dmytro, D_MENT