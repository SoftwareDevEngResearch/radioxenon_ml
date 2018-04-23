"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
from radioxenon_ml.tests import test_functions as tf
from read_in import ml_matrix_composition as mlmc

n=5
simulation_vec, experimental_vec, nrows, ncols = mlmc.form_matrix(n); 
tf.test_import_sizes(nrows, ncols,n)
        