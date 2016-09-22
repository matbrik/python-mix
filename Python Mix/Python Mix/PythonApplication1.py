from __future__ import print_function
import hashlib
import itertools as it
import string
import socket
from brainfuck import Nice


s = socket.socket()
s.connect(("lse.epita.fr", 52108))
data=s.recv(1024)+s.recv(1024)  
data=data.strip().split('\n')
print(data)
nice=Nice.NiceInterpreter()
nice.execute(data[1])
test=nice.array
print(test[2:7])
sum=0
for i in test[2:7]:
    sum*=10
    sum+=i-48

print(sum)

s = socket.socket()
s.connect(("lse.epita.fr", sum))
s.send(data[0].split(": ")[1])
rec=s.recv(1024)
print(rec)

nice=Nice.NiceInterpreter()
nice.execute(rec)
test=nice.array
print(test[2:7])
sum=0
for i in test[2:7]:
    sum*=10
    sum+=i-48

print(sum)

s = socket.socket()
s.connect(("lse.epita.fr", sum))
s.send(data[0].split(": ")[1])
rec=s.recv(1024)
print(rec)

while True:
    nice=Nice.NiceInterpreter()
    nice.execute(rec)
    test=nice.array
    print(test[2:7])
    sum=0
    for i in test[2:7]:
        sum*=10
        sum+=i-48
    
    print(sum)
    
    s = socket.socket()
    s.connect(("lse.epita.fr", sum))
    s.send(data[0].split(": ")[1])
    rec=s.recv(1024)
    print(rec)




"""   


for addr in lista:
    s = socket.socket()
    s.connect(("lse.epita.fr", 51108))
    c=0
    try:
        s.recv(5)
        s.close()
    except:
        s.close()
    print(addr)
    # stage 1: works
"""
