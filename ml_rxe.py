# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:25:47 2018

@author: Steven
"""

from radioxenon_ml.read_in import ml_matrix_composition as mlmc
from radioxenon_ml.solve import iterate
import radioxenon_ml.solve.iterate
import radioxenon_ml.solve.variance
"""the master file for the radioxenon_ml package"""

n=5 #this is a user defined number to state how many simulation spectra we will be using
spectrum_file_location = 'radioxenon_ml/test_files/test'
offset = 0  
err = 0.01

simulation, experiment = mlmc.form_matrix(spectrum_file_location,n,offset);    #known issue: requires UTF-8 encoding

iterate.iterate(simulation, experiment, err)