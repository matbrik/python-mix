"""
i ll try to use mechanize to scrape and automatize the bot  interest calculation with mechanize 

http://wwwsearch.sourceforge.net/mechanize/
"""


import re
import mechanize

def removeFrom(text, start, end):

    indexStart=text.find(start)
    indexEnd= text.find(end)
    return text[:indexStart]+ text[indexEnd:]

def request(data_e, data_r, taglio, div):
    br = mechanize.Browser()
    br.open("https://risparmiopostaleonline.poste.it/librettiOnLine/startCalcolatoreRendimentoBuonoFruttiferoAction.do")
    # follow second link with element text matching regular expression
    #response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
    assert br.viewing_html()

    
    
    br.select_form(name="ValoreRendimentoBuonoFruttiferoForm")
    
    br["selBuono"]=["O"]
    data_e_field = br.form.find_control(id="dataEmissione")
    data_e_field.value = data_e
    
    data_r_field = br.form.find_control(id="dataRimborso")
    data_r_field.value = data_r
    
    
    
    
    br["taglio"]=str(taglio)
    br["selDivisa"]=[div]
    
    
    
    br.find_control("selGiornoRimborso").readonly= False
    br.find_control("selMeseRimborso").readonly= False
    br.find_control("selAnnoRimborso").readonly= False
    
    br.find_control("selGiornoEmissione").readonly= False
    br.find_control("selMeseEmissione").readonly= False
    br.find_control("selAnnoEmissione").readonly= False
    
    de=data_e.split("/")
    dr=data_r.split("/")
    br["selGiornoRimborso"]= dr[0]
    br["selMeseRimborso"]=dr[1]
    br["selAnnoRimborso"]=dr[2]
    
    br["selGiornoEmissione"]= de[0]
    br["selMeseEmissione"]=de[1]
    br["selAnnoEmissione"]=de[2]
    
    
    
    request2 = br.click()  # mechanize.Request object
    try:
        response2 = mechanize.urlopen(request2)
    except mechanize.HTTPError, response2:
        pass
    
    text_page=response2.read()
    response2.close()
    text_page=removeFrom(text_page,"<!DOCTYPE ","netto**</strong> della ritenuta fiscale</td>")
    text_page=text_page[80: 100].strip()
    text_page=text_page.replace(".","")
    text_page=text_page.replace(",",".")
    val=float(text_page)

    return val


file = open("datimatteo.txt", "r")
records=file.readlines()
sum=0
result=open("risultatimatteo.txt","w")


for line in  records:
    line=line.replace("  "," ")
    tmp=line.strip().split(" ")
    res= request(tmp[0],"31/12/2020", int(tmp[1]) ,tmp[2])
    print(res)
    sum+=res
    print tmp


#t=request("20/01/2010","20/01/2017",1000,"EUR")
print(sum)

result.close()
file.close()


"""

<tr>
								<td class="sinistra">Valore del Buono al <strong>netto**</strong> della ritenuta fiscale</td>
								<td class="sinistra">
      
			1.000,00
	  		    
</td>
							</tr>
							<tr>
								<td class="sinistra">Rimborsi programmati di capitale</td>
								<td class="sinistra">
      
			0,00
	  		  
</td>
							</tr>


"""
"""
print response1.geturl()
print response1.info()  # headers
print response1.read()  # body

br.select_form(name="order")
# Browser passes through unknown attributes (including methods)
# to the selected HTMLForm.
br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
# Submit current form.  Browser calls .close() on the current response on
# navigation, so this closes response1
response2 = br.submit()

# print currently selected form (don't call .submit() on this, use br.submit())
print br.form

response3 = br.back()  # back to cheese shop (same data as response1)
# the history mechanism returns cached response objects
# we can still use the response, even though it was .close()d
response3.get_data()  # like .seek(0) followed by .read()
response4 = br.reload()  # fetches from server

for form in br.forms():
print form
# .links() optionally accepts the keyword args of .follow_/.find_link()
for link in br.links(url_regex="python.org"):
print link
    br.follow_link(link)  # takes EITHER Link instance OR keyword args
    br.back()
"""