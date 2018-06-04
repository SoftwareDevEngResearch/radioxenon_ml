"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
from radioxenon_ml.read_in import ml_matrix_composition as mlmc
from radioxenon_ml.solve import variance as v
from radioxenon_ml.solve import matrix_values as matval
import numpy as np

#for some reason the following import must occur in order to refresh any changes to variance 
#if I try to import it earlier it does not work
#this is a temporary thing, and is commented out when I am not actively testing functions
"""
import radioxenon_ml.solve.variance
import radioxenon_ml.read_in.ml_matrix_composition
import radioxenon_ml.solve.matrix_values
"""

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
    S = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]])
    A = np.array([[1,2,3,4,5]])
    f = np.array([[0,0,0,0,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,2,2,2,2,2,2],[2,2,2,2,2,2,3,3,3,3,3,3],[3,3,3,3,3,3,4,4,4,4,4,4],[0,1,0,0,1,0,2,3,1,0,0,0]]).T 
    for q in range(0,3):
        if q == 0:
            D=v.variance(q,S,f)
            assert len(D)==len(S)
            assert D[1] == S[2]
            print("\nFirst iteration is correct!")
        else:
            D=v.variance(q,A,f)
            assert np.shape(D)[0] == np.shape(f)[0]
            print("\nLengths are proper!")
            print(D)
        
def test_J():
    """
    Test to make sure the J vector comes out as a column of 4 isotopes + bkgd
    """
    S = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]])
    D = np.array([1,  1,  1,  1,  1,  1, 11, 11, 11, 11, 11, 11]).T
    f = np.array([[0,0,0,0,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,2,2,2,2,2,2],[2,2,2,2,2,2,3,3,3,3,3,3],[3,3,3,3,3,3,4,4,4,4,4,4],[0,1,0,0,1,0,2,3,1,0,0,0]]).T
  
    J=matval.j_matrix_val(S,D,f)
    assert np.shape(J)[0] == np.shape(f)[1]
    assert np.shape(J)[1] == 1
    print("\nJ column vector is correct!")
    print(J)
            
def test_K():
    """
    first test the K function using an experimental vector, then
    test the variance function using two known vectors
    """
    D = np.array([1,  1,  1,  1,  1,  1, 11, 11, 11, 11, 11, 11]) 
    f = np.array([[0,0,0,0,0,0,1,1,1,1,1,1],[1,1,1,1,1,1,2,2,2,2,2,2],[2,2,2,2,2,2,3,3,3,3,3,3],[3,3,3,3,3,3,4,4,4,4,4,4],[0,1,0,0,1,0,2,3,1,0,0,0]]).T
 
    K=matval.k_matrix_val(D,f)
    assert np.shape(K)[0] == np.shape(f)[1]
    assert np.shape(K)[1] == np.shape(f)[1]
    print("\nK Matrix is correct!")
    print(K)