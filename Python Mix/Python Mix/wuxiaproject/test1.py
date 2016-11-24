from lxml import html
import pdfkit
import requests
import unidecode

def page_parser(address):
    page = requests.get(address)

    tree = html.fromstring(page.content)
    prova= tree.xpath('//*[@id="main"]/article/div/div[1]/div/p/text()')
   
    out="\n".join(prova)
    return unidecode.unidecode(out)
    
page=""
file = open("newfile.txt", "w")
for i in range(208,400):
    file.write(str(i))
    page= page_parser("http://www.wuxiaworld.com/mga-index/mga-chapter-"+str(i))
    file.write(page)
    print(str(i) + "done")
file.close()

#pdfkit.from_string('Hello!', 'out.pdf')
# out = <your-unicode-text>

#print out
#//*article/div/div[1]/div/p[2]
