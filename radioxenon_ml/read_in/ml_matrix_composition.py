"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
from . import array_import as arr_im
import numpy as np

def form_matrix(n):
    
    nrowarr = np.empty(n+1, dtype=int)    #array for # of rows in each array
    ncolarr = np.empty(n+1, dtype=int)    #array for # of columns in each array
    
    for i in range(1,n+1):
        huzzah = open('test_files/test'+str(i)+'.csv')               #Opens file
        coin_arr = arr_im.load_2d_coinc_spectrum(huzzah)        #loads the array
        columnvec, nrowarr[i-1], ncolarr[i-1] = arr_im.vector_spectrum(coin_arr)    #turns into column
        
        if i==1:                        #efficiency of memory
            thearr = np.empty([(nrowarr[i-1]*ncolarr[i-1]),n])
        
        thearr[:,i-1] = columnvec[:,0]      #assemble the matrix
        
    print("Simulated spectra have been placed into the Maximum Liklihood Matrix")
    
    huzzah = open('test_files/test'+str(n+1)+'.csv')               #Opens experimental spectrum
    coin_arr = arr_im.load_2d_coinc_spectrum(huzzah)          #loads the array
    experimental_vec, nrowarr[n], ncolarr[n] = arr_im.vector_spectrum(coin_arr)    #turns into column
    print("Experimental have been placed into the Maximum Liklihood Matrix")
        
    return thearr, experimental_vec, nrowarr, ncolarr 