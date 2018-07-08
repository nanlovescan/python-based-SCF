#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:27:26 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: Build_Density
#Author: Nan Sheng

def Build_Density(C,Nel):
    
    length=np.size(C,1)
    D=np.mat(np.zeros((length,length)))
    m=np.arange(length)
    n=np.arange(length)
    p=np.arange(int(Nel/2))
    
    for i in m:
        for j in n:
            for k in p:
                D[i,j]=D[i,j]+2*C[i,k]*np.conj(C[j,k])
    return D
    