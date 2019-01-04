# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:21:10 2019

@author: Steven
"""
import matplotlib.pyplot as pp
import numpy as np

saveplot = 0
test_num = 81     #used for naming test spectra
rotate = 0

x_min = 0               #parameters for axes for plotting
y_min = 0
x_max = 1000
y_max = 400
bin_num_x = 500
bin_num_y = 200

spectrum_file_location = 'radioxenon_ml/test_files/test'  #file location
file_end ='.csv'

for test_num in range(11,85):
    my_data = np.genfromtxt(spectrum_file_location+str(test_num)+file_end, delimiter=',')
    
    #spectrum = np.zeros((np.amax(len(my_data)),np.amax(len(my_data))))
   
    
    if rotate == 1:
         spectrum = np.zeros((np.shape(my_data)[1],np.shape(my_data)[0]))
         for i in range(0,np.shape(my_data)[1]):
            spectrum[i,:] = my_data[:,i]
    else:
        spectrum = np.zeros(np.shape(my_data))
        for i in range(0,np.shape(my_data)[1]):
            spectrum[np.shape(my_data)[1]-i-1,:] = my_data[i,:]
        
    fig = pp.figure()    
    pp.xlabel('Summed energy deposited in PIPSBox (keV)')
    pp.ylabel('Summed energy deposited\n in SrI$_2$(Eu) (keV)')
    pp.ylim([0, np.amax(len(my_data))])
    pp.imshow(spectrum)
    pp.set_cmap('jet')
    pp.colorbar()
    
    if saveplot == 1:
        fig.savefig('radioxenon_ml/test_files/test' + str(test_num) + '.png', format='png')
    del fig
