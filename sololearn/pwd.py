#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:03:57 2018

@author: loc
"""

import string
from secrets import choice

alphabet = string.printable

def pwd(len=13):
    while True:
        pwd = ''.join(choice(alphabet) for i in range(len))
        if ((not any(c.isspace()) for c in pwd)
                and any(c.islower() for c in pwd)
                and any(c.isupper() for c in pwd)
                and any(c.isdigit() for c in pwd)
                and any(c.isprintable() for c in pwd)):
            break
    
    print(pwd)

if __name__ == "__main__":
    import sys
    pwd(int(sys.argv[1]))
