import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image
import bz2


if __name__ == '__main__':
    
    '''http://www.pythonchallenge.com/pc/return/5808.html'''
    img = Image.open('cave11.jpg')
    w, h = img.size
    org = img.load()

    imgs = [Image.new(img.mode, (w/2, h/2)) for dummy in xrange(4)]
    imgs_load = [i.load() for i in imgs]

    for i in xrange(w):
        for j in xrange(h):
            org_pos = (i, j)
            new_pos = (i//2, j//2)
            imgs_load[i%2 + j%2 * 2][new_pos] = org[org_pos]

    [imgs[i].save('leve11.%d.png' % i) for i in xrange(4)]
    
    
