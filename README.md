# webScrapper
A python 3 web Scrapper integrating request and BeautifullSoup

<h2>Scrapper.py</h2>

Its intended to be used in shell by passing arguments to get the desired part of website
params:
<ul>
<li>-u url # Target url</li>
<li>-t tag # Target tag, example a, li, p, span</li>
<li>-c classes # Target classes of the current target tag as a single string</li>
<li>-g text, href, img # It search for all elments matching tag/class params and return either the text value or the 
href value from a tag type a, img will download the src param from img tag</li>
</ul>
<h3>Examples</h3>
 <ul>
 <li> Getting href value from all a tags:<br>
<code>python3 Scrapper.py -u https://es.wikipedia.org -t a -c external -g href</code>
</li>
<li> Download all images from src param in img tags:<br>
<code>python3 Scrapper.py -u https://es.wikipedia.org -t img -g img</code>
</li>
</ul>
