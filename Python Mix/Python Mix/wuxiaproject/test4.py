import pdfkit
import requests
from PyPDF2 import PdfFileMerger
import unidecode

import os

def removeFrom(text, start, end):

    indexStart=text.find(start)
    indexEnd= text.find(end)
    return text[:indexStart]+ text[indexEnd:]


"""
alpha version

TODO remove comments in web pages

"""
start=700
end=1100
#name="WMW"
#address = "http://m.wuxiaworld.com/wmw-index/wmw-chapter-"

name="MGA"
address = "http://m.wuxiaworld.com/mga-index/mga-chapter-"





page = requests.get(address+str(start))
page2= unidecode.unidecode(unicode(page.content, "utf-8","ignore"))

section1=page2.find("<article id=\"post")#.find("</article>")
result=page2[:section1]
section2= page2.find("<div id=\"comments\"")
ending=page2[section2:]

result=removeFrom(result, "<div role=\"complementary\"","<div id=\"primary\"")
result=removeFrom(result, "<header","<div id=\"=page")

for i in range(start,end):
    page = requests.get(address+str(i))
    page2= unidecode.unidecode(unicode(page.content, "utf-8","ignore"))

    page2=removeFrom(page2,"<p><a title=","<hr/>\n<p><strong>")

    indexstart= page2.find("<article id=\"post")
    indexend= page2.find("<p><a")
    result+=page2[indexstart:indexend]+"</div></div></div></article>"
    print(str(i))


result+="</main></div></div></div></body></html>"
try:
    options = {
    
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in'
    }
    pdfkit.from_string(result, name+str(start)+"-"+str(end-1)+".pdf")
        
except IOError:
    pass 


