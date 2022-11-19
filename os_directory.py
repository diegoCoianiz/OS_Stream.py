from datetime import datetime
import calendar
import os
clear = lambda : os.system("cls")
clear()

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

#calendar.prcal(2022)


carp1 = "carpeta1"
carp2 = "carpeta2"

###########################################################################################################
                                                # CREATE DIRECTORY/IES
###########################################################################################################

def newDir(dirName, printListDir = True):
    try:
        os.mkdir(dirName)
        if printListDir : print(os.listdir())
    except:
        pass

def recursiveDirs(firstDirectory, secondDirectory, printListDir = True):
    try:
        os.makedirs(f"{firstDirectory}/{secondDirectory}")
        print(f"\tright now you are here: {os.getcwd()}")
        os.chdir(f"{firstDirectory}")
        print(os.getcwd())
        print(f"\tright now you are here: {os.getcwd()}")
    except:
        pass

os.mkdir("homeWork2")

###########################################################################################################
                                                # DELETE DIRECTORY
###########################################################################################################

def removeDir(dirName, printListDir = True):
    try:
        os.rmdir(dirName)
        if printListDir : print(os.listdir())
    except:
        pass

def removeRecursiveDirs(firstDirectory, secondDirectory, printListDir = True):
    try:
        os.removedirs(f"{firstDirectory}/{secondDirectory}")
        if printListDir : print(os.listdir())
    except:
        pass

