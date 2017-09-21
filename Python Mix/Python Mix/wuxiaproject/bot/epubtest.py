import pypub

import os
import requests
import unidecode


def removeFrom(text, start, end):

    indexStart=text.find(start)
    indexEnd= text.find(end)
    return text[:indexStart]+ text[indexEnd:]


"""
#test failed. the epub result was made of a page with the first link, a summary of the chap in the next one
epub=pypub.Epub("testww")
url="http://m.wuxiaworld.com/wmw-index/wmw-chapter-610/"
c=pypub.create_chapter_from_url(url)
epub.add_chapter(c)
epub.create_epub(os.getcwd())
"""


#i try to get the content of the page and insert it to an epub

name="WMW"
address="http://m.wuxiaworld.com/wmw-index/wmw-chapter-"
i=610



page = requests.get(address+str(i))
page2= unidecode.unidecode(unicode(page.content, "utf-8","ignore"))
if name=="MGA":
    page2=removeFrom(page2,"<p><a title=","<hr/>\n<p><strong>")
else:
    page2=removeFrom(page2,"<p><a href","<span style=\"text-decoration: underline\">")

indexstart= page2.find("<span style=\"text-decoration: underline\"><strong>")
indexend= page2.find("<p><a href=\"http://www.wuxiaworld.com/wmw-index/wmw-chapter-609/\">")
print(page2[indexstart:indexend])
print(str(i))

epub=pypub.Epub("testww")
c=pypub.create_chapter_from_string(page2[indexstart:indexend])
epub.add_chapter(c)
epub.create_epub(os.getcwd())