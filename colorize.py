#!python3
# colorize.py

import sys, urllib.request, re
from bs4 import BeautifulSoup


if len(sys.argv) <= 1:
    search = input('What would you like to colorize?  ')
else:
    search = sys.argv[1]
url = "https://alexbeals.com/projects/colorize/search.php?q="
page = urllib.request.urlopen(urllib.request.Request(url + search))
soup = BeautifulSoup(page, "html.parser")
color = re.findall(r'<span class=\"hex\">(.*)</span>', str(soup.findAll('span')[0]))[0]
print('Color:', str(color))
