import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image
import bz2
from cStringIO import StringIO

if __name__ == '__main__':
    '''http://www.pythonchallenge.com/pc/return/evil.html'''
    f = open('evil2.gfx', 'rb')
    sf = f.read()

    for i in xrange(5):
        f = open('evil12.d_0%d.jpg' % i, 'wb')
        f.write(sf[i::5])
        f.close()
    
    
    
