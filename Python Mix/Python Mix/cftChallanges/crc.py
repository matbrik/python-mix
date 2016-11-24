import httplib
import hashlib
import itertools as it
import string
import socket
from brainfuck import Nice
lista=[]
data1="sdsd"
conn= httplib.HTTPSConnection("dctf.def.camp")

while len(lista)<100:
    conn.request("GET", "/b4s1.php")
    r1=conn.getresponse()
    data1=r1.read().replace("<pre>","").replace("</pre>","")
    #print(data1)
    templist=[]
    for c in data1:
        templist.append(str(max(ord(c)%2,0)))
    print("".join(templist))

    if data1 in lista:
        print("Match:"+ data1)
        print(str(len(lista)))
        break;
    lista.append(data1)
    #if(len(lista)) > 500:
    #    break;

"""
s = socket.socket()
s.connect(("https://dctf.def.camp/b4s1.php", 80))
data=s.recv(1024)+s.recv(1024)  
data=data.strip().split('\n')
print(data)


"""