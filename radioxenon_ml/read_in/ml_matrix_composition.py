"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
from radioxenon_ml.read_in import array_import as arr_im
import numpy as np


def form_matrix(spectrum_file_location, scale_array = np.array([1,1,1,1,1,1,1]), n=5, offset=0):
    """
    Makes 4 arrays:
        1 column array for # of rows in each file
        1 column array for # of columns in each file
        1 column array for the single experimental spectrum
        1 nx5 array for the simulation spectra + background
        
    --spectrum_file_location(str): location of the files that are to be run. 
               The code expects the files to all be named the same name, with
               a number appended to it to represent the test file it is. For
               example, test1.csv, test2.csv, up to testn.csv. Starts from 1
    --n(int): number of spectra to be loaded. Default is 5 (4 simulated 
               radioxenon spectra plus one background spectrum)
   -- offset(int): how much of an offset from 1 for tests that you want to  
               load. This is primarily useful if you have many tests (say 1-9),
               but you only want to load 4-8. You would put in offset = 3 and 
               set n=5
    """    
    nrowarr = np.empty(n+1, dtype=np.int32)    #define array for # of rows in each array
    ncolarr = np.empty(n+1, dtype=np.int32)    #define array for # of columns in each array
    
    for i in range(1,n+1):
        opened_spec_file = open(spectrum_file_location+str(i+offset)+'.csv')               
        coin_arr = arr_im.load_2d_coinc_spectrum(opened_spec_file)                            #loads the array
        coin_arr = np.round(coin_arr*scale_array[i-1]);
        columnvec, nrowarr[i-1], ncolarr[i-1] = arr_im.vector_spectrum(coin_arr)    #turns into column
        
        if i==1:                        
            simulation_arr = np.empty([(nrowarr[i-1]*ncolarr[i-1]),n], dtype=np.int32)           #define array for simulation data
        
        simulation_arr[:,i-1] = columnvec[:,0]      #assemble the matrix one column at a time
        
    print("\nSimulated spectra have been placed into the Maximum Likelihood Matrix")
    
    opened_spec_file = open(spectrum_file_location+str(n+1+offset)+'.csv')           #Opens experimental spectrum
    coin_arr = arr_im.load_2d_coinc_spectrum(opened_spec_file)                       #loads the array
    #experimental_vec = np.empty(columnvec.shape[0], dtype=int)                      
    experimental_vec, nrowarr[n], ncolarr[n] = arr_im.vector_spectrum(coin_arr)     #turns into column
    print("\nExperimental have been placed into the Maximum Likelihood Matrix")
        
    return simulation_arr, experimental_vec
