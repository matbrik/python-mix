#!/bin/python3
import sys

def recursive_search(lista_lista_nodi, depth, array_rif, node):
    if depth==0 or len(array_rif)==0:
        return array_rif
    array_rif=set(array_rif)-set(lista_lista_nodi[node])
    for e in lista_lista_nodi[node]:
        if len(array_rif)==0:
            return array_rif
        array_rif=recursive_search(lista_lista_nodi,depth-1,array_rif,e)
    return array_rif

n=20
m=4
# your code goes here


# your code goes here
q=0
res=""
lista_lista_nodi=[]
for q in range(n):
    lista=[]
    lista.append((q+1)%n)
    res+=str((q+1)%n)
    for w in range(1,m-1):
        e=int(round(((n-3)*w)/(m-2+1)-0.49))
        e+=q+2
        e=e%n
        lista.append(e)
        res+=" "+str(e)

        
    res+=" "+str((q-1)%n)+"\n"
    lista.append((q-1)%n)
    lista_lista_nodi.append(lista) 
depth=0
array_rif=[]
for i in range(n):
    array_rif.append(i)
while(len(array_rif)!=0):
    depth+=1
    array_rif=[]
    visited=[]
    for i in range(n):
        array_rif.append(i)
    array_rif=recursive_search(lista_lista_nodi, depth, array_rif, n//2)
    print(array_rif)
print(str(depth))
print(res)