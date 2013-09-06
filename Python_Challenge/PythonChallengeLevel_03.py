import urllib2

f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')

data = f.read()

import re

reg = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
comtextReg = re.compile('<!--[\W\w]*-->')

s_str_01 = ''.join(comtextReg.findall(data))
print s_str_01
print ''.join(reg.findall(data))
print ''.join(reg.findall(s_str_01))
