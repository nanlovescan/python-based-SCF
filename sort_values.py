#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:57:29 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: sort_values
#Author: Nan Sheng

def sort_values(C,epsilon):
    length=np.size(C,1)
    index=np.argsort(epsilon)
    epsilon=np.sort(epsilon)
    eigenvecs=np.mat(np.zeros((length,length)))

    for i in np.arange(length):
        eigenvecs[:,i]=C[:,[index[i]]]
    C=eigenvecs
    return C,epsilon
    
    
    
    
    
    
    
    
    






