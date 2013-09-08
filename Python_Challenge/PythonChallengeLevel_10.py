import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image
import bz2

def getList(str):
    list = []
    
    if str:
        list = [str[0]]
        for i in range(1, len(str), 1):
            if list[len(list) - 1][0] == str[i]:
                tem = list[len(list) - 1]
                tem = tem + str[i]
                list[len(list) - 1] = tem
                pass
            else:
                list.append(str[i])
                pass
        pass
    else:
        pass
    print list
    return list

def getStr(list):
    mystr = ''
    for x in list:
        mystr = mystr + str(len(x)) + x[0]

    return mystr

if __name__ == '__main__':
    
    '''http://www.pythonchallenge.com/pc/return/bull.html'''
    a = ['1']
    for x in range(1, 31, 1):
        mystr = getStr(getList(a[x-1]))
        a.append(mystr)
        pass
    print a[30]
    print len(a[30])
