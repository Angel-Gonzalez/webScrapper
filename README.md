# webScrapper
A python 3 web Scrapper integrating request and BeautifullSoup

Scrapper.py

Its intended to be used in shell by passing arguments to get the desired part of website
params:
-u <url> # Target url
-t <tag> # Target tag, example <a>some link</a>
-c <classes> # Target classes of the current target tag as a single string
-g <text or href> # It search for all elments matching tag/class params and return either the text value or the href value from a tag type <a>

Example full query:
python3 Scrapper.py -u https://es.wikipedia.org -t a -c external -g href
