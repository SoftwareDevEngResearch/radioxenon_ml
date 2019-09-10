# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:19:53 2018

@author: Steven
"""

import numpy as np

def j_matrix_val(S,D,f):
    """
    Determines the variance of the number of counts in each channel i of the 
    vectorized version of the 2D coincidence spectrum for the qth iteration:
        
    -S(np.array) is the original experimental spectrum
    -D(np.array) is the determined variance value from variance()
    -f(np.array) is the reference spectrum for each isotope as well as background
    
    Equations are taken from the quite excellent paper:
        
        Lowrey, Justin D., and Steven R.F. Biegalski. “Comparison of Least-
        Squares vs. Maximum Likelihood Estimation for Standard Spectrum 
        Technique of Β−γ Coincidence Spectrum Analysis.”  Nuclear Instruments 
        and Methods in Physics Research Section B: Beam Interactions with 
        Materials and Atoms 270 (January 2012): 116–19. 
        https://doi.org/10.1016/j.nimb.2011.09.005.
        
    """
    J_temp = np.zeros((np.shape(f)[1],np.shape(f)[0]))
    J = np.zeros((np.shape(f)[1],1))

    for j in range(np.shape(f)[1]):        #loop over # of isotopes
        for i in range(np.shape(f)[0]):         #loop over # of array elements
            J_temp[j,i] = (S[i]*f[i,j])/D[i]   #Eqn. 7
        
        J[j] = np.sum(J_temp[j])    #sum all columns to make a column vector
                    
    return J

def k_matrix_val(D,f):
    """
    Determines the variance of the number of counts in each channel i of the 
    vectorized version of the 2D coincidence spectrum for the qth iteration:
        
    -D(np.array) is the determined variance value from variance()
    -f(np.array) is the reference spectrum for each isotope as well as background
    
    Equations are taken from the quite excellent paper:
        
        Lowrey, Justin D., and Steven R.F. Biegalski. “Comparison of Least-
        Squares vs. Maximum Likelihood Estimation for Standard Spectrum 
        Technique of Β−γ Coincidence Spectrum Analysis.”  Nuclear Instruments 
        and Methods in Physics Research Section B: Beam Interactions with 
        Materials and Atoms 270 (January 2012): 116–19. 
        https://doi.org/10.1016/j.nimb.2011.09.005.
        
    """
    K_element_temp = np.zeros((np.shape(f)[1],np.shape(f)[0]))
    K = np.zeros((np.shape(f)[1],np.shape(f)[1]))
    

    for m in range(np.shape(f)[1]):        #loop over # of isotopes
        for j in range(np.shape(f)[1]):        #loop over # of isotopes again
            for i in range(np.shape(f)[0]):         #loop over # of array elements
                K_element_temp[j,i] = (f[i,m]*f[i,j])/D[i]   #Eqn. 7
    
            K[m,j] = np.sum(K_element_temp[j])  #sum all elements to make an entry in the array
    
    return K
