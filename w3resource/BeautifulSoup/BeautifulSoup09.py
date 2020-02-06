import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.python.org')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first a tag:")
h2_tags = soup.find_all("h2")
for i in range(4):
    print(h2_tags[i].text)
