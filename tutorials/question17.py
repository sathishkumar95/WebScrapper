import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
#print(soup)
#print(soup.title)
titles = soup.find_all(class_='story-heading')
for pagetitles in titles:
    if pagetitles.a:
        print(pagetitles.a.text.replace("\n"," ").strip())
    else:
        print(pagetitles.contents[0].strip())

