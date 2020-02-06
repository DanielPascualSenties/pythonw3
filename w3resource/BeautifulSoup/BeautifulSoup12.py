import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.python.org')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')


print(soup.get_text())