# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:07:40 2016

@author: Leonard
"""

def Esp2(conf, t):
    m2=0
    siz=(np.size(conf,1))-1
    if t < 15: #On ne veut pas calculer tous les moments c'est trop long, on commence à t = 15 
                #De toute façon le premier moment n'est pas stable avant...
        return 0
    else:
        for i in range(siz+1):
            for j in range(siz+1):
                for k in range(siz+1):
                    for l in range(siz+1):
                        m2 = m2+conf[i][j]*conf[k][l]
        return m2/N**2
    
def Esp4(conf, t):
    m4=0
    siz=(np.size(conf,1))-1
    if t<15: #Pareil que pour m2
        return 0
    else:
        for i in range(siz+1):
            for j in range(siz+1):
                for k in range(siz+1):
                    for l in range(siz+1):
                        for m in range(siz+1):
                            for n in range(siz+1):
                                for o in range(siz+1):
                                    for p in range(siz+1):
                                        m4 = m4+conf[i][j]*conf[k][l]*conf[m][n]*conf[o][p]