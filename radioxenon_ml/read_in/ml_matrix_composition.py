"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
from radioxenon_ml.read_in import array_import as arr_im
import numpy as np

"""
Makes 4 arrays:
    1 column array for # of rows in each file
    1 column array for # of columns in each file
    1 column array for the single experimental spectrum
    1 nx5 array for the simulation spectra + background
"""
def form_matrix(n):
    
    nrowarr = np.empty(n+1, dtype=np.int32)    #define array for # of rows in each array
    ncolarr = np.empty(n+1, dtype=np.int32)    #define array for # of columns in each array
    
    for i in range(1,n+1):
        huzzah = open('radioxenon_ml/test_files/test'+str(i)+'.csv')               
        coin_arr = arr_im.load_2d_coinc_spectrum(huzzah)                            #loads the array
        columnvec, nrowarr[i-1], ncolarr[i-1] = arr_im.vector_spectrum(coin_arr)    #turns into column
        
        if i==1:                        
            thearr = np.empty([(nrowarr[i-1]*ncolarr[i-1]),n], dtype=np.int32)           #define array for simulation data
        
        thearr[:,i-1] = columnvec[:,0]      #assemble the matrix one column at a time
        
    print("\nSimulated spectra have been placed into the Maximum Liklihood Matrix")
    
    huzzah = open('radioxenon_ml/test_files/test'+str(n+1)+'.csv')                                #Opens experimental spectrum
    coin_arr = arr_im.load_2d_coinc_spectrum(huzzah)                                #loads the array
    experimental_vec = np.empty(columnvec.shape[0], dtype=int)                      #defines experimental array
    experimental_vec, nrowarr[n], ncolarr[n] = arr_im.vector_spectrum(coin_arr)     #turns into column
    print("\nExperimental have been placed into the Maximum Liklihood Matrix")
        
    return thearr, experimental_vec, nrowarr, ncolarr 