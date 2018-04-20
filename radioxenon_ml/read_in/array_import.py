"""
Created on Fri Apr 20 13:00:43 2018

@author: Steven
Topic: array importer
"""
import numpy as np

def load_2d_coinc_spectrum(inputfile):
    coincidence_array = np.genfromtxt(inputfile, delimiter = ',', dtype='int', encoding='utf-8-sig')  #encodes file as float
    return coincidence_array
    print('Coincidence spectrum read and returned as an array!')

def vector_spectrum(inputarray):
    [rows,columns] = inputarray.shape
    vec_spec = np.reshape(inputarray,[rows*columns,1])
    return vec_spec
    print('Coincidence array turned into a column vector!')
    
    
    
huzzah = 'test1.csv'
coin_arr = load_2d_coinc_spectrum(huzzah)
test_vec = vector_spectrum(coin_arr)
#print(coincidence_array)