import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.python.org')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first a tag:")
h2_tags = soup.find_all("a")
for i in range(10):
    print(h2_tags[i].attrs['href'])
