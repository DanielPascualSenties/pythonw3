import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.python.org')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first a tag:")
li = soup.find_all("li")
for i in li:
    a = i.find('a')
    print(a.attrs['href'])
