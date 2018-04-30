"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
from radioxenon_ml.read_in import ml_matrix_composition as mlmc

def test_different_n_values():
    """
    test_different_n_values() makes sure that various values of n can be loaded into the file without it breaking
    """
    
def test_array_clear():
    """
    test_array_clear() ascertains that each run of form_matrix() outputs the appropriate files
    """
    n = 5
    spectrum_file_location = 'radioxenon_ml/test_files/test'

def test_import_sizes():    
    """
    test_import_sizes() makes sure the number of rows and number of columns vectors are uniform
    """
    n = 5
    spectrum_file_location = 'radioxenon_ml/test_files/test'
    simulation_vec, experimental_vec = mlmc.form_matrix(n,spectrum_file_location,offset)
    for i in range(0,n-1):
        assert numberofrows[i] == numberofrows[i+1]
        assert numberofcols[i] == numberofcols[i+1]
        
    print("\nNo assertion errors for import sizes; all input files identical")
    return

def test_two_matrices():                        #passes is there are two matrices formed
    """
    test_two_matrices() makes sure two matrices have been formed
    spectrum_file_location = file location of the dummy files, size 6x5
    """
    n = 5
    spectrum_file_location = 'radioxenon_ml/test_files/test'
    simulation_vec, experimental_vec = mlmc.form_matrix(n)
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
