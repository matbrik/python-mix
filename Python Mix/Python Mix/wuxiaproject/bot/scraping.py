import xlsxwriter
import pdfkit
import requests
import unidecode
import os

from bs4 import BeautifulSoup




def removeFrom(text, start, end):

    indexStart=text.find(start)
    indexEnd= text.find(end)
    return text[:indexStart]+ text[indexEnd:]
"""
def removeFrom(text,start):
    indexStart=text.find(start)
    return text[indexStart+len(start):]
"""


def getChapterList(address,last):
    while(1):
        page = requests.get(address+str(last))
        print("ok")
        soup=BeautifulSoup(page.content,'html.parser')
        title=soup.find("title")
        print(title)
        
        if str(title).startswith("<title>Page not found"):
            print(":(")
            return last-1
        else:
            print(":)")
            last+=1
"""
    input_list=soup.find("select", {"name": "chapter_list"})
    input_list = input_list.find_all("option")
    chapter_numbers=[]
    for e in input_list:
        chapter_numbers.append(removeFrom(str(e["value"]).strip(),address))

    return chapter_numbers[1:]
"""





def create_page(address,name, start, end):
    
        
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
        pdfkit.from_string(result, name+str(start)+"-"+str(end)+".pdf")
        return unidecode.unidecode(unicode(name+str(start)+"-"+str(end)+".pdf", "utf-8","ignore"))  
            
    except IOError:
        return unidecode.unidecode(unicode(str(name+str(start)+"-"+str(end)+".pdf"), "utf-8","ignore"))  

              
 



