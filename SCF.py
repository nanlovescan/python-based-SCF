# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt    

#Theme: Self Consistent Field
#Author: Nan Sheng

def SCF(S,T,V,gabcd,Nel):
    import e1, e2, sort_values, Build_Density, Build_Coulomb_Exchange, Fock_Energy
    
    maxcycle=1000
    ncycle=0
    converged=0
    
    S=e1.e1(S)
    T=e1.e1(T)
    V=e1.e1(V)
    gabcd=e2.e2(gabcd)
    H0=T+V

    s,R=np.linalg.eig(S)
    s=np.power(s,(-1/2))
    s=np.mat(np.diag(s))
    X=R*s*(R.H)
    F=H0
    Fprime=(X.H)*F*X
    epsilon,Cprime=np.linalg.eig(Fprime)
    C=X*Cprime
    C,epsilon=sort_values.sort_values(C,epsilon)
    D=Build_Density.Build_Density(C,Nel)
    E=np.zeros((maxcycle,1))
    
    while (ncycle<maxcycle) and (converged!=1):
        G=Build_Coulomb_Exchange.Build_Coulomb_Exchange(D,gabcd)
        F=H0+G
        Fprime=(X.H)*F*X
        epsilon,Cprime=np.linalg.eig(Fprime)
        Cprime,epsilon=sort_values.sort_values(Cprime,epsilon)
        C=X*Cprime
        C,epsilon=sort_values.sort_values(C,epsilon)
        D=Build_Density.Build_Density(C,Nel)
        E[ncycle]=Fock_Energy.Fock_Energy(D,F,H0)
        if (ncycle>0) and (np.abs(E[ncycle]-E[ncycle-1]) < 10**(-100)):
            converged=1
        else: converged=0
        ncycle=ncycle+1
            
    E=E[:(ncycle),0]
    Emin=E[ncycle-1]
    
    print('ncycle =',ncycle)
    print('E =',E)
    print('Emin =',Emin)  
    print('D =',D)  
    
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    