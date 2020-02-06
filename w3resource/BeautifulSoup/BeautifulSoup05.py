import urllib

from bs4 import BeautifulSoup
from urllib import request

page = urllib.request.urlopen('https://www.marca.com')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Text in the first paragraph:")
#first_h2 = soup.find_all("h2")[0].text
#print(first_h2)

h2s = soup.find_all("h2")
for i in h2s:
    print(i.text)
