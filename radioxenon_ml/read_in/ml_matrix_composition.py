"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
from . import array_import as arr_im

def form_matrix(x):
    huzzah = open('tests/test'+str(x)+'.csv', "r+b")            #Opens file
    coin_arr = arr_im.load_2d_coinc_spectrum(huzzah)            #loads the array
    columnvec, ncol, nrow = arr_im.vector_spectrum(coin_arr)    #turns into column
        
    return columnvec, ncol, nrow