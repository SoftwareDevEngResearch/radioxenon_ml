# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""

def test_import_sizes(numberofrows, numberofcols):
    for i in range(0,5):
        assert numberofrows[i] == numberofrows[i+1]
        assert numberofcols[i] == numberofcols[i+1]
        