import pdfkit
import requests
import unidecode


from bs4 import BeautifulSoup


full_url="http://m.wuxiaworld.com/wmw-index/wmw-chapter-1045/"




page=requests.get(full_url)
page2= unidecode.unidecode(unicode(page.content, "utf-8","ignore"))

soup=BeautifulSoup(page2,'html.parser')
[s.extract() for s in soup('iframe')]
[s.extract() for s in soup('link')]

[s.extract() for s in soup('script')]

soup.find(id="comments").extract()

soup.find(id="masthead").extract()

soup.find(id="secondary").extract()

soup.find(id="colophon").extract()

soup.find(id="text-41").extract()




main_page=unidecode.unidecode(unicode(str(soup), "utf-8","ignore"))



options= {
    'run-script': "setInterval(function(){if(document.readyState=='complete') window.status='done';},100)" ,
    'window-status':'done',
    'page-size': 'A6',
    'margin-top': '0.0in',
    'margin-right': '0.0in',
    'margin-bottom': '0.0in',
    'margin-left': '0.0in'
}
#pdfkit.from_url(full_url,"out.pdf", options=options)
pdfkit.from_string(main_page,"out.pdf", options=options)
