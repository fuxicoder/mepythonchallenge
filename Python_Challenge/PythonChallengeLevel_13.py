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
    '''http://www.pythonchallenge.com/pc/return/disproportional.html'''
    xmlrpc = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print xmlrpc.phone('Bert')
    
    
    
