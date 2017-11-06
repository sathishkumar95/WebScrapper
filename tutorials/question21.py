import requests
from bs4 import BeautifulSoup
url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
#print(soup)
#print(soup.title)
content = ''
with open('NewyorkTimes.txt','w') as open_file:
    titles = soup.find_all(class_='story-heading')
    for pagetitles in titles:
        if pagetitles.a:
            content += pagetitles.a.text.replace("\n"," ").encode('utf-8').strip()
            content += "\n"
        else:
            content += pagetitles.contents[0].encode('utf-8').strip()
            content += "\n"
    open_file.write(content)

