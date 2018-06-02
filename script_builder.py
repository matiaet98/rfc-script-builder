#!/bin/python
import os
import threading

__author__ = 'Estevez Matias Exequiel'

def getRFCs(myFile):
    theFile = open(myFile,'r')
    rfcs = theFile.readlines()
    theFile.close()
    rfcs = [x.rstrip() for x in rfcs]
    return rfcs

def buildScript(theList,theFile):
    newFile = open(theFile,'w')
    newFile.write('set define off;\n')
    for x in theList:
        os.chdir(x)
        newFile.writelines(['@'+x+'/'+f+'\n' for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))])
        os.chdir('..')
    newFile.write('/')
    newFile.close()


def main():
    sefi = getRFCs('sefi.txt')
    fisco = getRFCs('fisco.txt')
    threading.Thread(target=buildScript, args=(sefi,'sefi_script.sql')).start()
    threading.Thread(target=buildScript, args=(fisco,'fisco_script.sql')).start()
    #buildScript(sefi,'sefi_script.sql')
    #buildScript(fisco,'fisco_script.sql')
    
if __name__ == "__main__":
    main()