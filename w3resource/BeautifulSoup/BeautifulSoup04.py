import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.marca.com')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first paragraph:")
first_paragraph = soup.find_all("p")[0].text
print(first_paragraph)
