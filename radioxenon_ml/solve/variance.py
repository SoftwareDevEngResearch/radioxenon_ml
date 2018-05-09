# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:15:54 2018

@author: Steven
"""
import numpy as np

def variance(q, AS, f):
    """
    Determines the variance of the number of counts in each channel i of the 
    vectorized version of the 2D coincidence spectrum for the qth iteration:
        
    -q is the iteration number
    -AS is either the estimated activity of the kth nuclide A or 
        the experimental sample spectrum S (if first iteration)
    -f is the reference spectrum
    
    Equations are taken from the quite excellent paper:
        
        Lowrey, Justin D., and Steven R.F. Biegalski. “Comparison of Least-
        Squares vs. Maximum Likelihood Estimation for Standard Spectrum 
        Technique of Β−γ Coincidence Spectrum Analysis.”  Nuclear Instruments 
        and Methods in Physics Research Section B: Beam Interactions with 
        Materials and Atoms 270 (January 2012): 116–19. 
        https://doi.org/10.1016/j.nimb.2011.09.005.
        
    """
    D_temp = np.zeros((len(AS),len(f)))
    D = np.zeros(len(f))
    
    if q < 0:
        print("Iteration must be greater than 0! Exiting...")
        return 
    
    else:      
        if q > 0:
            for k in range(len(AS)):        #loop over # of isotopes
                for i in range(len(f)):         #loop over # of array elements
                    D_temp[k,i] = AS[k]*f[i]   #Eqn. 5
            
            D = np.sum(D_temp,axis=0)  
            
        else:
            D = AS+1
        
        return D
