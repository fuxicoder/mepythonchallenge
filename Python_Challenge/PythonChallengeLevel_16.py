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

def getX(img, y):
    for x in xrange(w):
        if img.getpixel((x, y)) == (255, 0, 255, 255):
                return x
    return 0
if __name__ == '__main__':
    '''http://www.pythonchallenge.com/pc/return/mozart.html'''
    im_s = Image.open('mozart.png')
    im_s_load = im_s.load()
    im_d = Image.new(im_s.mode, im_s.size, (0, 0, 0, 255))
    print im_s.mode

    im_d_d = Image.new(im_s.mode, im_s.size)
    w, h = im_s.size

    for y in xrange(h):
        d = getX(im_s, y)
        for x in xrange(w):
            if x < d:
                im_d.putpixel((w - d + x, y), im_s.getpixel((x, y)))
                pass
            else:
                im_d.putpixel((x - d, y), im_s.getpixel((x, y)))
            
            
    im_d.save('mozart.png.png')
    
    
    
    
    
