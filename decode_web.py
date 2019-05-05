from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

r_parsed = BeautifulSoup(r_html)
r_title = str(r_parsed.find('span', 'articletitle'))