"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
from radioxenon_ml.read_in import ml_matrix_composition as mlmc
from radioxenon_ml.solve import variance as v
import numpy as np


def test_file_existence():
    """
    test_file_existence() makes sure that the file one is trying to load in exists
    """
    spectrum_file_location = 'radioxenon_ml/test_files/test' 
    attempted_file_load=1
    for offset in range(0,8):
        try: 
            open(spectrum_file_location+str(attempted_file_load)+'.csv') #this is the "experiment" file
        except FileNotFoundError:
            print(attempted_file_load)
            assert attempted_file_load==0 
        
    
def test_different_n_values():
    """
    test_different_n_values() makes sure that various values of n can be loaded into the file without it breaking
    Checks if the file exists, then loads it in
    n is set to 1 permenantly such that only one file at a time gets loaded
    If offset is 7 or above, an error should occur
    """
    spectrum_file_location = 'radioxenon_ml/test_files/test' 
    n=1
    for offset in range(0,6):
        try:
            first_sim_vec, first_exp_vec = mlmc.form_matrix(spectrum_file_location,n,offset)
        except FileNotFoundError:
            print(n+1+offset)
            assert n==0
    
def test_array_clear():
    """
    test_array_clear() ascertains that each run of form_matrix() outputs the appropriate files
    This is done by using two different offsets with an n of 1
    This should break if the two offsets load files that are not of identical dimensions, which occurs if you try to load file 7
    """
    n = 1
    offset = 3
    spectrum_file_location = 'radioxenon_ml/test_files/test'
    first_sim_vec, first_exp_vec = mlmc.form_matrix(spectrum_file_location,n,offset)
    offset = 4
    second_sim_vec, second_exp_vec = mlmc.form_matrix(spectrum_file_location,n,offset)
    print(np.shape(first_exp_vec))
    print(np.shape(second_exp_vec))
    assert np.shape(first_sim_vec) == np.shape(second_sim_vec)
    assert np.shape(first_exp_vec) == np.shape(second_exp_vec)
    print("\nNo assertion errors for import sizes; all input files identical")
    

def test_two_matrices():                        #passes is there are two matrices formed
    """
    test_two_matrices() makes sure two matrices have been formed
    spectrum_file_location = file location of the dummy files, size 6x5
    """
    spectrum_file_location = 'radioxenon_ml/test_files/test'
    simulation_vec, experimental_vec = mlmc.form_matrix(spectrum_file_location)
    assert 'experimental_vec' in locals()
    assert 'simulation_vec' in locals()
    
    print("\nBoth the simulation matrix and the measurement matrix exist!")
    return

def matrix_legitimacy():
    """
    matrix_legitimacy() makes sure the matrices are legitimate, i.e.: they've loaded the right data
    spectrum_file_location = file location of the dummy files, size 6x5
    """
    n = 5
    spectrum_file_location = 'radioxenon_ml/test_files/test'
    simulation_vec, experimental_vec = mlmc.form_matrix(n,spectrum_file_location)
    assert simulation_vec[0,0] == 1
    assert simulation_vec[29,0] == 30
    assert simulation_vec[29,4] == 150
    assert simulation_vec.dtype == 'int32'
    assert experimental_vec.shape[0] == 30
    assert experimental_vec[23] == 11
    
    print("\nBoth the simulation matrix and the measurement matrix are of correct dimensions\nand were correctly built!")
    return

def test_variance():
    """
    first test the variance function using an experimental vector, then
    test the variance function using two known vectors
    """
    S = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    A = np.array([1,1,1,1,2,2,2,2,3,3,3,3])
    f = np.array([0,0,0,0,0,0,1,1,1,1,1,1])
    D=np.array([])   
    for q in range(0,3):
        if q == 0:
            D=np.append(D,v.variance(q,S,f))
        else:
            D=np.append(D,v.variance(q,A,f))
        print(D)
    
        