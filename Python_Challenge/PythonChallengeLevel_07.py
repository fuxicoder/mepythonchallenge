import sys
import string
import urllib2
from  xml.dom import  minidom
import webbrowser as wb
import re
import Image

if __name__ == '__main__':
    f = open("oxygen.png", 'wb')
    f.write(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read())
    f.close()
    
    i = Image.open('oxygen.png')
    print i.size

    row = [i.getpixel((x, i.size[1]/2)) for x in range(0, i.size[0], 7)]
    ords = [r for r, g, b, a in row if r == g == b]
    print "".join(map(chr, ords))
    print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))
