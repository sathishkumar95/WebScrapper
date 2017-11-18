# -*- coding: utf-8 -*-
import requests

import psycopg2
import ctypes
import re
from scrapy.http import HtmlResponse


def convertint(content):
    temp = ""
    x = re.findall(r'\d+', content)
    for i in x:
        temp += str(i)
    var = temp
    return var

def getresponseobj(url):
    body = requests.get(url).text
    response = HtmlResponse(url=url, body=body, encoding='utf-8')
    return response


def connectdb():
    connect_str = "dbname='justdial' user='intern' host='34.211.197.118' password='prime123'"
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor

def closedbconnection(conn, cursor):
    cursor.close()
    conn.close()


def parse_result(response):
    cursor1 = connectdb()
    vendor = response.xpath('//div[@id="sellerName"]/a/@title').extract()
    name = re.findall(r'\w+', str(vendor))
    print name[1]
    product_name = response.xpath('//h1[@class="_3eAQiD"]/text()[1]').extract()
    rating = response.xpath('//div[@class="CamDho"]/text()').extract()
    content = []
    dict = {}
    for j in rating:
        temp = ""
        # j = j.encoding('utf-8')
        x = re.findall(r'\d+', j)
        for i in x:
            temp += str(i)
        content.append(temp)
    dict = {
        '5_star': content[0],
        '4_star': content[1],
        '3_star': content[2],
        '2_star': content[3],
        '1_star': content[4],
    }
    print dict

    try:
        update = "UPDATE products SET stars=%s where product_name=%s;"
        updatedata = (str(dict),product_name[0])
        cursor1.execute(update,updatedata)
        try:
            query = "INSERT INTO flk_seller(vendor_name,hash, product_key) VALUES (%s,%s,'');"
            hashcode = str(ctypes.c_size_t(hash(str(name) + "flipkart")).value)
            name = str(name[1])
            data = (name, hashcode)
            cursor1.execute(query, data)
        except Exception as e:
            print("this is due to multiple sellers ")
            print e


    except Exception as e:
        print("part 2 sql queries caused this")
        print(e)

hashcodelst = []


start_urls = 'https://www.flipkart.com/air-conditioners/pr?otracker=categorytree&page=1&sid=j9e%2Cabm%2Cc54&viewType=list'
vendorlink = 'http://www.flipkart.com/seller/omnitechretail/c82e1fb314f34969'
response = getresponseobj(start_urls)
product_name = response.xpath('//div[@class="_3wU53n"]/text()').extract()
product_Id = response.xpath('//div[@class="OiPjke"]/text()').extract()
product_price = response.xpath('//div[@class="_6BWGkk"]/div/div[1]/text()[2]').extract()
ratings = response.xpath('//span[@class="_38sUEc"]/span[1]/span[1]/text()').extract()
reviews = response.xpath('//span[@class="_38sUEc"]/span[1]/span[3]/text()').extract()
links = response.xpath('//a[@class="_1UoZlX"]/@href').extract()
start = "https://www.flipkart.com"

try:

    cursor = connectdb()
    query = "INSERT INTO products(product_name,product_code,price,rating,reviews,hash,stars) VALUES( %s, %s, %s, %s, %s, %s, %s);"

    for item in zip(product_name, product_Id, product_price, ratings, reviews, links):
        dict = {
            'name': item[0],
            'id': item[1],
            'price': item[2],
            'rating': item[3],
            'review': item[4],
            'link': item[5],
        }
        print dict

        #call fetch response function to get the details
        parse_result(getresponseobj(start+item[5]))

        hashcode = str(ctypes.c_size_t(hash(item[0] + "flipkart")).value)


        #content = []
        hashcodelst.append(hashcode)
        numrating = convertint(item[3])
        numreview = convertint(item[4])
        print("\n\n\n\n\nname :%s \n\nid :%s \n\nprice :%s \n\nrating :%s \n\nreview : %s " % (
            item[0], item[1], item[2], numrating, numreview))
        try:
            data = [item[0], item[1], item[2], numrating, numreview, hashcode, '']
            cursor.execute(query, data)
        except Exception as e:
            print("SQl queries caused this")
            print(e)


    rep = getresponseobj(vendorlink)
    stars = rep.xpath('//ul[@class="rating-histogram"]/li/text()[3]').extract()
    content=[]
    for j in stars:
        temp = ""
        # j = j.encoding('utf-8')
        x = re.findall(r'\d+', j)
        for i in x:
            temp += str(i)
        content.append(temp)
    dict = {
        '5_star': content[0],
        '4_star': content[1],
        '3_star': content[2],
        '2_star': content[3],
        '1_star': content[4],
    }
    update = "UPDATE flk_seller SET product_key=%s;"
    hashdata = (hashcodelst,)
    cursor.execute(update, hashdata)
    update = "UPDATE flk_seller SET stars=%s;"
    hashdata = (str(dict),)
    cursor.execute(update,hashdata)



except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password? first try error")
    print(e)








