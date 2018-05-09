# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:29:08 2018

@author: Steven
"""
from radioxenon_ml.solve import variance as v
from radioxenon_ml.solve import matrix_values as matval
import numpy as np

def iterate(f,S,err=0.01):
    """
    Conducts the iterative process to determine the relative activities of
    radioxenon isotopes and of background in the experimental spectrum
        
    -S(np.array) is the experimental spectrum
    -f(np.array) is an array of the reference spectra for the reference spectra k
    -err(float) is the acceptable variance before exiting the iteration scheme
    
    Equations are taken from the quite excellent paper:
        
        Lowrey, Justin D., and Steven R.F. Biegalski. “Comparison of Least-
        Squares vs. Maximum Likelihood Estimation for Standard Spectrum 
        Technique of Β−γ Coincidence Spectrum Analysis.”  Nuclear Instruments 
        and Methods in Physics Research Section B: Beam Interactions with 
        Materials and Atoms 270 (January 2012): 116–19. 
        https://doi.org/10.1016/j.nimb.2011.09.005.
        
    """
    
    q=0
    Aold = np.ones((1,np.shape(f)[0]))/np.shape(f)[0]  #normalized beginning activity array
    stop_iteration = 0
    
    while stop_iteration == 0:
        
        if q==0:
            D = v.variance(q,S,f)
        else:
            D = v.variance(q,Aold,f)
        
        J = matval.j_matrix_val(S,D,f)
        K = matval.k_matrix_val(D,f)
        
        A = np.transpose(np.linalg.solve(K, J))
        
        compare_error = abs((A-Aold)/A)
        
        if np.min(compare_error) >= err:
        
            Aold = A
            q += 1
            
        else:
            
            print(compare_error)