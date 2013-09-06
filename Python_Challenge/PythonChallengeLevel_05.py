import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import pickle

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

data = f.read()
print data
obj = pickle.loads(data)
print obj

for list in obj:
    print(''.join(t[0] * t[1] for t in list))
    
    
a = [(1,2),(3,4),(5,6),(7,8),(9,0),(10,11)]
print a
b = pickle.dumps(a)
print b
c = pickle.loads(b)
print a

'''
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
'''
    
