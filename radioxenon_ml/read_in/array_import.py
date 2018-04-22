"""
Created on Fri Apr 20 13:00:43 2018

@author: Steven
Topic: array importer
"""
import numpy as np

def load_2d_coinc_spectrum(inputfile):
    coincidence_array = np.genfromtxt(inputfile, delimiter = ',', dtype='int')  #encodes file as float
    print('Coincidence spectrum read and returned as an array!')
    return coincidence_array

def vector_spectrum(inputarray):
    [rows,columns] = inputarray.shape
    vec_spec = np.reshape(inputarray,[rows*columns,1])
    print('Coincidence array turned into a column vector!')
    return vec_spec, rows, columns
    