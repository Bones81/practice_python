import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, features='html.parser')
titlesFound = soup.findAll('h3')
titles = []

def extractTitles(rawSoup):
    for title in rawSoup:
        titles.append(title.string)

extractTitles(titlesFound)

for title in titles:
    print(title)