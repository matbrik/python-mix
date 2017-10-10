
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
    page = requests.get(address)
    soup=BeautifulSoup(page.content,'html.parser')
    lista=[]
    article_list=soup.find_all("article")
    for article in article_list:
        id=article.get("id")
        id=id[5:]
        e=article.find("a")
        lista.append([id,e.get("href")])
    return lista

#1
import iointerface
import json
import time


fn="riv.txt"

lista=json.loads(iointerface.readFile(fn))
print(lista)