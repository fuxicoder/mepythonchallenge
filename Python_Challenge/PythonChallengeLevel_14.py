import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image
import bz2
from cStringIO import StringIO
import xmlrpclib  

if __name__ == '__main__':
    '''http://www.pythonchallenge.com/pc/return/italy.html'''
    
    n = 100
    im = Image.new('RGB', (n, n))
    wire = Image.open('wire.png')
    count = 0
    for x in range(n*2):
        y = x//4
        first = y+1
        last = n-y
        if x%4 == 0:
            first -= 1
        if x%4 == 3:
            last -= 1
        for i in range(first, last):
            im.putpixel((i, y), wire.getpixel((count+i-first, 0)))        
        im = im.rotate(90)
        count += last - first
    im.save('wire.png.png')
    
    
    
    
