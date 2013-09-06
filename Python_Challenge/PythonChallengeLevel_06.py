import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import pickle
import os
import zipfile

def getFileName(num):
    strFileName = "channel/%s.txt" % (num)
    return strFileName
def isFileExist(strFileName):
    flag = os.path.exists(strFileName)
    return flag
def getNumFromFile(strFileName):
    f = open(strFileName, "r")
    reg = re.compile('[0-9]{1,}')
    s = f.readline()
    list = reg.findall(s)
    f.close()
    if list:
        return list.pop()
        pass
    else:
        return 1
        pass
def getStrFromFile(strFileName):
    f = open(strFileName, "r")
    s = f.read()
    f.close()
    return s
    
def fun_step_01():
    flag = True
    num = 90052
    while flag:
        strFileName = getFileName(num)
        print num
        print strFileName
        if isFileExist(strFileName):
            num = getNumFromFile(strFileName)
            if num == 1:
                print getStrFromFile(strFileName)
                flag = False
            else:
                pass
            pass
        else:
            flag = False
def fun_step_02():
    z = zipfile.ZipFile('channel.zip', mode='r')
    prefix = '90052'
    surfix = '.txt'
    findNothing = re.compile('Next nothing is (\d*)').search
    comments = []
    while True:
        text = z.read(prefix + surfix)
        print(text)
        match = findNothing(text)
        print match
        if match:
            prefix = match.group(1)
            comments.append(z.getinfo(prefix + surfix).comment)
        else:
            break
    print(''.join(comments))
    
if __name__ == '__main__':
    fun_step_02()


    
