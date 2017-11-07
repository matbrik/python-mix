import requests
from readability import Document
import unidecode


response= requests.get("http://www.wuxiaworld.com/mga-index/mga-chapter-2152/")
response= unidecode.unidecode(unicode(response.content, "utf-8","ignore"))

doc= Document(response)

print(doc.summary())