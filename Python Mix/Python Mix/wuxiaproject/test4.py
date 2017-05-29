import pdfkit
import requests
from PyPDF2 import PdfFileMerger
import unidecode



from bs4 import BeautifulSoup


import os

def removeFrom(text, start, end):

    indexStart=text.find(start)
    indexEnd= text.find(end)
    return text[:indexStart]+ text[indexEnd:]


"""
alpha version

TODO remove comments in web pages

"""
start=662
end=665
name="WMW"
address = "http://m.wuxiaworld.com/wmw-index/wmw-chapter-"

#name="MGA"
#address = "http://m.wuxiaworld.com/mga-index/mga-chapter-"





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
    if name=="MGA":
        page2=removeFrom(page2,"<p><a title=","<hr/>\n<p><strong>")
    else:
        page2=removeFrom(page2,"<p><a href","<span style=\"text-decoration: underline\">")

    indexstart= page2.find("<article id=\"post")
    indexend= page2.find("<div id=\"comments\"")
    print(page2[indexstart:indexend])
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
    soup=unidecode.unidecode(unicode(str(result), "utf-8","ignore"))  
    pdfkit.from_string(str(soup), name+str(start)+"-"+str(end-1)+".pdf")
        
except IOError:
    pass 


