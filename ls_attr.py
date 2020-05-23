#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2018/06/06
@author Lôc Cosnier

List available modules and the functions associated
Better to try within the Python shell or as a script
"""

from pkgutil import iter_modules
from importlib import import_module
from inspect import getmembers, isfunction

#List available modules excluding those who begin by _ 
for mod in iter_modules():
    if mod[1][0] != "_":
        print(mod[1] + ": ", end = "")
        #For each module, try to import it to get all the functions associated
        #excluding those who begin by _
        try:
            module = import_module(mod[1])
            list = [x for x in getmembers(module, isfunction) if x[0][0] != "_"]
            if list != []:
                for l in list:
                    print(l[0] + ", ", end = "")
        except Exception as e:
            print(e)
        print("\n")
