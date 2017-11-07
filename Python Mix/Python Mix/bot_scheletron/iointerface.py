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