import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php')

data = f.read()
print data
reg = re.compile("nothing=[0-9]*")
regNum = re.compile("[0-9]{1,}")

s_str_url_o = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
s_str_01 = ''.join(reg.findall(data))
s_str_arry_01 = s_str_01.split('=')
s_str_02 = s_str_arry_01.pop();

str_str_url = s_str_url_o + s_str_02
print str_str_url
flag = True

while flag:
    fa = urllib2.urlopen(str_str_url)
    data = fa.read()
    print data
    str_list = regNum.findall(data)
    if str_list:
        s_str_02 =  str_list.pop()
        print s_str_02
        str_str_url = s_str_url_o + s_str_02
        pass
    else:
        flag = False
        pass

    print str_str_url

flag = True

s_str_02 = regNum.findall(str_str_url).pop()
s_str_02 = int(s_str_02) / 2
str_str_url = s_str_url_o  + str(s_str_02)

while flag:
    print str_str_url
    fa = urllib2.urlopen(str_str_url)
    data = fa.read()
    print data
    str_list = regNum.findall(data)
    if str_list:
        s_str_02 = str_list.pop();
        print s_str_02
        str_str_url = s_str_url_o + s_str_02
        pass
    else:
        flag = False
        pass
str_str_url = "http://www.pythonchallenge.com/pc/def/" + data
print str_str_url
wb.open(str_str_url)
    
