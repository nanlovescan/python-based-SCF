#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 11:17:06 2018

@author: nathansheng

Description:
"""
import numpy as np
import matplotlib.pyplot as plt    

#Theme: Build_Coulomb_Exchange
#Author: Nan Sheng

def Build_Coulomb_Exchange(D,gabcd):
    
    length=np.size(D,1)
    G=np.mat(np.zeros((7,7)))
    m=np.arange(length)
    n=np.arange(length)        
    p=np.arange(length)
    q=np.arange(length)
    
    for a in m:
        for b in n:
            for c in p:
                for d in q:
                    G[a,b]=G[a,b]+D[c,d]*(gabcd[a,b,d,c]-0.5*np.conj(gabcd[a,c,d,b]))
    return G



    
    
    
    