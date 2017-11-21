import PyPDF2

file ='table.pdf'
pfr = PyPDF2.PdfFileReader(open(file, "rb"))
pdfReader = PyPDF2.PdfFileReader(pfr)
print pdfReader.getNumPages()