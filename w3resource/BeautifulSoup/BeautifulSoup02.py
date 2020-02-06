from bs4 import BeautifulSoup
import urllib.request

page = urllib.request.urlopen('http://www.marca.com/')
st = page.read()
soup = BeautifulSoup(st, 'html.parser')
print("Paragraph tags:")
paragraphs = soup.find_all("p")
for i in paragraphs:
    print(i)
