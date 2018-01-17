import requests
from scrapy.http import HtmlResponse

url = "http://www.moneycontrol.com/news/business/stocks/"

def getresponseobj(url):
    body = requests.get(url).text
    response = HtmlResponse(url=url, body=body, encoding='utf-8')
    return response


def get_last_updateTime(response):
    time = response.css('#newslist-0 > span').extract()
    print(time)
    return time


if __name__ == "__main__":
    response = getresponseobj(url)
    time = get_last_updateTime(response)
    #fetch_news()