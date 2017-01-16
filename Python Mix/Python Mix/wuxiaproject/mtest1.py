from fpdf import FPDF
import urllib
from PIL import Image

def resize(x,y):
    rx=x/595.0
    ry=y/842.0
    if(rx<1 and ry < 1):
        return x,y
    if(rx>ry):
        x=x/rx
        y=y/rx
    if(ry>rx):
        x=x/ry
        y=y/ry
    return int(x),int(y)


import requests
pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
# imagelist is the list with all image filenames

pdf.add_page()
urllib.urlretrieve("http://funmanga.com/uploads/chapters/15395/93/1.jpg", "tmp.jpg")
im=Image.open("tmp.jpg")
print im.size
r=resize(im.size[0],im.size[1]) 
im.thumbnail(r, Image.ANTIALIAS)
im.save("tmp.jpg", "JPEG")
pdf.image("tmp.jpg",r)
pdf.output("yourfile.pdf", "F")