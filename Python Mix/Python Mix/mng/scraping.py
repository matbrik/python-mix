
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

def removeFrom(text,start):
    indexStart=text.find(start)
    return text[indexStart+len(start):]



def getChapterList(address):
    page = requests.get(address+str(1))
    print("ok")
    soup=BeautifulSoup(page.content,'html.parser')
    input_list=soup.find("select", {"name": "chapter_list"})
    input_list = input_list.find_all("option")
    chapter_numbers=[]
    for e in input_list:
        chapter_numbers.append(removeFrom(str(e["value"]).strip(),address))

    return chapter_numbers[1:]



"""

def create_page(address, list_of_chapters):
    num=list_of_chapters[0]
    num2=list_of_chapters[len(list_of_chapters)-1]
    page = requests.get(address+str(num)+"/all-pages")
    soup=BeautifulSoup(page.content,'html.parser')
    for t in soup.findAll("script"):
        t.decompose()
    class_to_delete="col-md-12 col-top clearfix chapter-toolbox","col-md-12 col-top clearfix","header","footer","footer","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4"
    for c in class_to_delete:
        t=soup.find("div",class_=c)
        t.decompose()
    main_page=soup

    for c in list_of_chapters[1:]:
        page = requests.get(address+str(c)+"/all-pages")
        soup=BeautifulSoup(page.content,'html.parser')
        class_to_delete="col-md-12 col-top clearfix chapter-toolbox","col-md-12 col-top clearfix","header","footer","footer","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4"
        for e in class_to_delete:
            t=soup.find("div",class_=e)
            t.decompose()
        tag=soup.find("div",class_="content")
        main_page.body.append(tag)
    try:
        options = {

        'margin-top': '0.0in',
        'margin-right': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in'
        }
        main_page=unidecode.unidecode(unicode(str(main_page), "utf-8","ignore"))
        pdfkit.from_string(main_page, "onepiece"+"_"+str(num)+"-"+str(num2)+".pdf")

    except IOError:
        pass
"""
def create_page(address, name, chapter):
    num=chapter
    page = requests.get(address+str(num)+"/all-pages")
    soup=BeautifulSoup(page.content,'html.parser')
    for t in soup.findAll("script"):
        t.decompose()
    class_to_delete="col-md-12 col-top clearfix chapter-toolbox","col-md-12 col-top clearfix","header","footer","footer","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4","col-lg-4 col-md-4 col-sm-4 col-xs-4"
    for c in class_to_delete:
        t=soup.find("div",class_=c) 
        t.decompose()
    main_page=soup
    try:
        options = {

        'margin-top': '0.0in',
        'margin-right': '0.0in',
        'margin-bottom': '0.0in',
        'margin-left': '0.0in'
        }
        main_page=unidecode.unidecode(unicode(str(main_page), "utf-8","ignore"))
        pdfkit.from_string(main_page, name+"_"+str(num)+".pdf")
        return unidecode.unidecode(unicode(str(name+"_"+str(num)+".pdf"), "utf-8","ignore"))
    except IOError:
        pass



