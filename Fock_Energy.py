#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:31:37 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: 
#Author: Nan Sheng

def Fock_Energy(D,H0,F):
    E=0
    length=np.size(D,1)
    m=np.arange(length)
    n=np.arange(length)
    for a in m:
        for b in n:
            E=E+0.5*D[a,b]*(H0[b,a]+F[b,a])
    return E
