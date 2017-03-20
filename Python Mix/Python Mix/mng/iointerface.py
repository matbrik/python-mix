import io
import json
"""
Of each manga i need the address, the name, the last chapter read
"""

#returns a json object dumped, use loads to recover the dictionary
def readFile(fileName):
    file=open(fileName,"r")
    records="".join(file.readlines())
    file.close()
    return records


#records: json object dumped
def writeFile(fileName, records):
    file = open(fileName,"w")
    file.write(records)
    file.close()



def testIO():
    lista=[]
    lista.append({"url":"htpp", "name":"pippo","last_chap":30})
    lista.append({"url":"htpp", "name":"pippo","last_chap":31})
    lista.append({"url":"htpp", "name":"pippo","last_chap":32})
    fn="test.txt"
    t=json.dumps(lista)

    writeFile(fn, t)
    t=readFile(fn)
    o=json.loads(t)
    print(o)
    