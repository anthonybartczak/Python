from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="html.parser")
print(soup)


for story_heading in soup.find_all(class_="balancedHeadline"):
    print(story_heading)