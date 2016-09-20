from __future__ import print_function
import hashlib
import itertools as it
import string
import socket

    

stringtmp="1234567890qwertyuiopasdfghjklzxcvbnm<>,.;:-_òàù+è§°çé*#@[]{}ì'^?=)(/&%$£\"!|"
i=0
tmp=""
lista=[42001,
42109,
42315,
42316,
42326,
42327,
42329,
42338,
42350,
42358,
42368,
42370,
42373,
42382,
42383,
42386,
42387,
42389,
42391,
42394
]
lista2=[]
for addr in lista:
    s = socket.socket()

    s.connect(("lse.epita.fr", addr))
    c=0
    try:
        s.recv(5)
        s.close()
    except:
        s.close()
    print(addr)
    # stage 1: works

