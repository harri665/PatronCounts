import os
import shutil
from git import Repo
import requests
import base64

url = 'https://pastebin.com/raw/bB4wBAPP'
req = requests.get(url)
tx = 0 
curVersion = 1.1
versionIN = 0 
versionIN = float(req.text)

def LoadVerion(): 
    global curVersion
    FileVersion = open("Version.txt" , "r")
    txin = 0
    for line in FileVersion:
        if(txin == 0):
            curVersion = float(line)
        txin += 1 
            
def SaveVersion(Vs): 
    FileSave = open("Version.txt" ,"w")
    FileSave.write(str(Vs))


dir = 'Program/'
def Add():
    print("added")
    os.makedirs("Program")
    Repo.clone_from("https://github.com/harri665/PatronCounts", "Program")
    print("ADDED ALL ")
def Delete():
    if os.path.isdir(dir):
        os.system('rmdir /S /Q "{}"'.format(dir))
        shutil.rmtree(dir, ignore_errors=True)
        print("deletedALL")
def CheckNeedUpdate(): 
    if(curVersion < versionIN):

        return True
    else:
        print("retuned flase")
        return False


def RunMainUpdate():
    print("Started")
    LoadVerion()
    if os.path.isdir(dir):
        if(curVersion < versionIN):
            Delete()
            Add() 
            SaveVersion(versionIN)
            print("updated!")
        else:
            print("no need for update")

    else:
        Add()

def main():

    RunMainUpdate()



if __name__ == "__main__":
    main()
