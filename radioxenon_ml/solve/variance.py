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
    """
    if q < 0:
        print("Iteration must be greater than 0! Exiting...")
        return 
    else:
        if q > 0:
            D = np.sum(AS*f)
        else:
            if len(AS) != len(f):
                print("Please make your two arrays of equal length! Exiting...")
                return 
            else:
                D = AS+1
        
        return D
