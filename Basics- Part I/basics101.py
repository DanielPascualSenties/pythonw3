import requests


def clean_title(line: str):
    place = line.rfind("title")
    after = line[place+7:]
    end = after.find('"')
    done = after[:end]
    # done = after
    return done


print("Write the URL you want to parse")
# link = str(input())
link = "http://www.marca.com"
f = requests.get(link)
rawText = f.text
# print(rawText)
lines = rawText.split('\n')
print(len(lines))
titles = list(filter(lambda x: 'title="' in x, lines))
titles = map(clean_title, titles)
print(*titles, sep='\n')
