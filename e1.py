#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:26:29 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: e1
#Author: Nan Sheng

def e1(N):
    length=np.size(N,0)
    P=N[:,:2].astype(int)
    M=np.mat(np.zeros((7,7)))
    for i in np.arange(length):
        M[P[i,0]-1,P[i,1]-1]=N[i,2]
        M[P[i,1]-1,P[i,0]-1]=N[i,2]
    return M
    
    
    
    