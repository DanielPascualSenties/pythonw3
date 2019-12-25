import urllib.request

page = urllib.request.urlopen('http://www.marca.com/')
st = page.read()

