"""
Created on Sun Apr 22 17:24:47 2018

@author: Steven
"""

def test_import_sizes(numberofrows, numberofcols,n):
    for i in range(0,n-1):
        assert numberofrows[i] == numberofrows[i+1]
        assert numberofcols[i] == numberofcols[i+1]
        
    print("No assertion errors for import sizes; all input files identical")
    return

def test_two_matrices():
    assert 'experimental_vec' in locals()
    assert 'simulation_vec' in locals()
    
    print("Both the simulation matrix and the measurement matrix exist!")
    return