#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 12:56:21 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: e2
#Author: Nan Sheng

def e2(N):
    length=np.size(N,0)
    P=N[:,:4].astype(int)
    M=np.zeros((7,7,7,7))
    for i in np.arange(length):
        M[P[i,0]-1,P[i,1]-1,P[i,2]-1,P[i,3]-1]=N[i,4]
        M[P[i,1]-1,P[i,0]-1,P[i,2]-1,P[i,3]-1]=N[i,4]
        M[P[i,0]-1,P[i,1]-1,P[i,3]-1,P[i,2]-1]=N[i,4]
        M[P[i,1]-1,P[i,0]-1,P[i,3]-1,P[i,2]-1]=N[i,4]
        M[P[i,2]-1,P[i,3]-1,P[i,0]-1,P[i,1]-1]=N[i,4]
        M[P[i,3]-1,P[i,2]-1,P[i,0]-1,P[i,1]-1]=N[i,4]
        M[P[i,2]-1,P[i,3]-1,P[i,1]-1,P[i,0]-1]=N[i,4]
        M[P[i,3]-1,P[i,2]-1,P[i,1]-1,P[i,0]-1]=N[i,4]
    return M
    
    