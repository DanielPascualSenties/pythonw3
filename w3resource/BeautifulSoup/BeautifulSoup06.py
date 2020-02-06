import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.marca.com')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first a tag:")
first_a_tag = soup.find_all("a")[0].text
print(first_a_tag)
