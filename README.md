# webScrapper
A python 3 web Scrapper integrating request and BeautifullSoup

Scrapper.py

Its intended to be used in shell by passing arguments to get the desired part of website
params:
<ul>
<li>-u url # Target url</li>
<li>-t tag # Target tag, example a, li, p, span</li>
<li>-c classes # Target classes of the current target tag as a single string</li>
<li>-g text or href # It search for all elments matching tag/class params and return either the text value or the 
href value from a tag type a</li>
</ul>
Example full query: 
<code>python3 Scrapper.py -u https://es.wikipedia.org -t a -c external -g href</code>
<br>this will return all <a> tags with a class "external" getting the href value of them
