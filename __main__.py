"""
Created on Sun April 22 13:24:00 2018

@author: Steven Czyz
"""
from radioxenon_ml.read_in import ml_matrix_composition as mlmc

n=5 #this is a user defined number to state how many simulation spectra we will be using
spectrum_file_location = 'radioxenon_ml/test_files/test'
offset = 0  

print(type(n))
print(type(spectrum_file_location))

simulation_vec, experimental_vec = mlmc.form_matrix(spectrum_file_location, n);    #known issue: requires UTF-8 encoding

