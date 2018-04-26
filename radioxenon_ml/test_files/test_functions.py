"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""
from radioxenon_ml.read_in import ml_matrix_composition as mlmc


"""
test_import_sizes() makes sure the number of rows and number of columns vectors are uniform
"""
def test_import_sizes():    
    n = 5
    _, _, numberofrows, numberofcols = mlmc.form_matrix(n)
    for i in range(0,n-1):
        assert numberofrows[i] == numberofrows[i+1]
        assert numberofcols[i] == numberofcols[i+1]
        
    print("\nNo assertion errors for import sizes; all input files identical")
    return

"""
test_two_matrices() makes sure two matrices have been formed
"""
def test_two_matrices():                        #passes is there are two matrices formed
    n = 5
    simulation_vec, experimental_vec, _, _ = mlmc.form_matrix(n)
    assert 'experimental_vec' in locals()
    assert 'simulation_vec' in locals()
    
    print("\nBoth the simulation matrix and the measurement matrix exist!")
    return

"""
matrix_legitimacy() makes sure the matrices are legitimate, i.e.: they've loaded the right data
"""
def matrix_legitimacy():
    n = 5
    simulation_vec, experimental_vec, _, _ = mlmc.form_matrix(n)
    assert simulation_vec[0,0] == 1
    assert simulation_vec[29,0] == 30
    assert simulation_vec[29,4] == 150
    assert simulation_vec.dtype == 'int32'
    assert experimental_vec.shape[0] == 30
    assert experimental_vec[23] == 11
    
    print("\nBoth the simulation matrix and the measurement matrix are of correct dimensions\nand were correctly built!")
    return
