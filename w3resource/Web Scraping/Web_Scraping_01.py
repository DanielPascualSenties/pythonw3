from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen("https://marcraakhjsbdaksdjba.com")
except HTTPError as e:
    print("HTTP error")
    print(e)
except URLError as e:
    print("Server not found!")
    print(e)
else:
    print(html.read())
