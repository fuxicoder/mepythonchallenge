import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image
import bz2  

if __name__ == '__main__':
    f = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/integrity.html')
    urlData = f.read()
    print urlData

    name  = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    passwd = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    print 'name = %s' % bz2.decompress(name)
    print 'password = %s' % bz2.decompress(passwd)
