from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import scraperwiki
import re
from tabula import read_pdf

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text



def pdf_to_html(path):
    with open(path) as w:
        x = scraperwiki.pdftoxml(w.read())
        print x


def pdf_tabula(path):
    df = read_pdf(path)
    print df

if __name__=='__main__':
    path = '/home/primenumbers/Documents/hal.pdf'
    var = convert_pdf_to_txt(path)
    #print(var)
    output = re.findall(r'(?<=Sub: )(.*)\n',str(var))
    ref = re.findall(r'(?<=Tender Ref No: )(.*)\n',str(var))
    ref = str(ref[0])
    length = len(ref) / 2
    Date = ref[length:]
    print("Tender : %s" % output[0])
    print("Tender ref no : %s" % ref[:length])
    print("%s" % Date.strip())
    #pdf_to_html(path)
    pdf_tabula(path)


