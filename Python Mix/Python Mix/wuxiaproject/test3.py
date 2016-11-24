import pdfkit
import requests
from PyPDF2 import PdfFileMerger
import unidecode

import os
"""
alpha version

TODO remove comments in web pages

"""
start=300
end=400
#name="WMW"
#address = "http://m.wuxiaworld.com/wmw-index/wmw-chapter-"

name="MGA"
address = "http://m.wuxiaworld.com/mga-index/mga-chapter-"








for i in range(start,end):
    page = requests.get(address+str(i))
    page2= unidecode.unidecode(unicode(page.content, "utf-8","ignore"))
    print("step1")

    indexstart= page2.find("<div id=\"comments\" class=\"comments-area\">")
    print("step2")
    #end=page2.find("<div role=\"complementary\">\n<div class='ai-viewport-2'>")
    end=page2.find("<footer id=\"colophon\" class=\"site-footer\" role=\"contentinfo\">")
    print("step3")
    endpage=page2[end:]
    l1=endpage.find("<script")
    print("step4")
    endpage=endpage[:l1]+"</body></html>"
    page3 = page2[:indexstart]+ endpage
    print("step5")
    try:
    # do stuff
    # and more stuff
        pdfkit.from_string(page3, "out"+str(i)+".pdf")
        
    except IOError:
    # do this
        pass    
    
    print(str(i))

merger = PdfFileMerger()

for i in range(start,end):
    merger.append("out"+str(i)+".pdf")

merger.write(name+str(start)+"-"+str(end-1)+".pdf")
merger.close()
for i in range(start,end):
    os.remove("out"+str(i)+".pdf")

