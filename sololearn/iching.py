#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:38:16 2018

@author: Lôc Cosnier
"""

from urllib.request import urlopen
from random import randint
from html.parser import HTMLParser
import re

diag = randint(1, 64)

url = "http://wengu.tartarie.com/wg/wengu.php?l=Yijing&no=" + str(diag)

class Parser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.record_prose = 0
        self.prose = ""
    
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            for name, value in attrs:
                if name == 'class' and value == 'prose_comment':
                    self.record_prose = 1 
    
    def handle_endtag(self, tag):
        self.record_prose -= 1

    def handle_data(self, data):
        if self.record_prose == 1:
            self.prose = data    


parser = Parser()
text = urlopen(url).read().decode("big5")
parser.feed(text)
print("Hexagram: {0}".format(str(diag)))
regex = re.compile(r'[\n\r\t]')
print(regex.sub('', parser.prose))
parser.close()