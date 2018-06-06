# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 09:54:07 2018

@author: Steven
"""
import matplotlib.pyplot as pp
import numpy as np


x_min = 0           #parameters for axes for plotting
y_min = 0
x_max = 1000
y_max = 1000
bin_num = 100

spectrum_file_location = 'radioxenon_ml/spectrum_gen/'  #file location
file_end ='_coin.txt'

for i in range(0,6):    #plot all 6 radioxenon files
    if i == 0:
        isotope = '131m'
    elif i == 1:
        isotope = '133m'
    elif i == 2:
        isotope = '135'
    elif i == 3:
        isotope = '133gb'
    elif i == 4:
        isotope = '133xb'
    elif i == 5:
        isotope = '133xe'

    #read out coincidence data and scale by 1000 (to put into keV instead of MeV)
    c_data = np.loadtxt(spectrum_file_location+isotope+file_end, skiprows=1)    
    c_data[:,(2,3)] *= 1000
    
    #Gaussian broadening
    c_data[:,(2,3)] = np.random.normal(c_data[:,(2,3)], (0.17/2.35)*c_data[:,(2,3)])
    
    # pp.ax.set_title('axes title')
    pp.xlabel('Summed energy deposited in PIPSBox (keV)')
    pp.ylabel('Summed energy deposited in SrI$_2$(Eu) (keV)')
    pp.hist2d(c_data[:,3],c_data[:,2], bins=bin_num, range=[[x_min,x_max],[y_min,y_max]])
    pp.set_cmap('jet')
    pp.colorbar()
    pp.show()

