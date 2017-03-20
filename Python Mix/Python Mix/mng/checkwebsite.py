"""
I'm using aws to handle the periodic check of the website
"""
from __future__ import print_function

from bs4 import BeautifulSoup
import requests
import boto3
import unidecode
import pdfkit


import os
 
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
 


SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable


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
        pdfkit.from_string(main_page, "/tmp/onepiece"+"_"+str(num)+"-"+str(num2)+".pdf")
        return "completed"    
    except IOError:
        pass 
    
    

def lambda_handler(event, context):
    print('Checking {}'.format(SITE))
    try:
        print(getChapterList(SITE))
        address="http://www.readmanga.today/one-piece1/"
        print(create_page(address,[1]))
        
    except:
        print('Check failed!')
        raise
    finally:
        print('Check complete ')
