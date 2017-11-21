import scraperwiki
import lxml
from lxml import etree
path = '/home/primenumbers/Documents/hal.pdf'
with open(path) as w:
    x = scraperwiki.pdftoxml(w.read())
    print x
    """x = x.encode('utf-8')
    r = lxml.etree.fromstring(x)
    res = r.xpath('//page[@number="1"]')
    text = r.xpath('//text[@left="64"]/b')[:20]
    for i in text:
        print i.text"""
