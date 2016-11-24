import pdfkit
import requests
from PyPDF2 import PdfFileMerger
import os
"""
alpha version

TODO remove comments in web pages

"""
start=400
end=500
#name="WMW"
#address = "http://m.wuxiaworld.com/wmw-index/wmw-chapter-"

name="MGA"
address = "http://m.wuxiaworld.com/mga-index/mga-chapter-"

for i in range(start,end):
    pdfkit.from_url(address+str(i), "out"+str(i)+".pdf")
#page = requests.get(address)

#pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfFileMerger()

for i in range(start,end):
    merger.append("out"+str(i)+".pdf")

merger.write(name+str(start)+"-"+str(end-1)+".pdf")
merger.close()
for i in range(start,end):
    os.remove("out"+str(i)+".pdf")

