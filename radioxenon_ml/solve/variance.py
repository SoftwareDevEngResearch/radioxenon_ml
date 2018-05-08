# -*- coding: utf-8 -*-
"""
Created on Mon May  7 22:15:54 2018

@author: Steven
"""
import numpy as np

def variance(q, AS, f):
    """
    Determines the variance of the number of counts in each channel 
    i for the qth iteration, where:
        -q is the iteration number
        -AS is either the estimated activity of the kth nuclide A or 
            the experimental sample spectrum S (if first iteration)
        -f is the reference spectrum
    
    Equation is taken from
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
