#beautiful soup and request

from bs4 import BeautifulSoup
import requests

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
print(soup)


