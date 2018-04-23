"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
import read_in.ml_matrix_composition as mlmc

n=5 #this is a user defined number to state how many simulation spectra we will be using

simulation_vec, experimental_vec, nrows, ncols = mlmc.form_matrix(n);    #known issue: requires UTF-8 encoding

