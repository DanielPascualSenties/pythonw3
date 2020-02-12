import requests, bs4, webbrowser

# Downloading the html of the selected website
website = requests.get('https://club.wien.at/angebote/gewinnspiele/')


# Retrieve links
gewinnspiele = bs4.BeautifulSoup(website.text, 'html.parser')

print(gewinnspiele)
# Open a browser tab for each link with the class below
linkElems = gewinnspiele.select('.cta ctaIcon ctaIconNoText')

print(len(linkElems))


#for i in range(2):
#    webbrowser.open('https://club.wien.at/' + linkElems[1].get('href'))