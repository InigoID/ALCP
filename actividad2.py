# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 23:43:36 2022

@author: Iñigo Iriondo Delgado
"""

import numpy as np

def conway(l,m,n,k):
    for i1 in range(k):
        mundo = np.zeros((m,n))
        for i2 in range(m):
           for i3 in range(n):
               if vecinos(l,i2,i3,n,m)==3:
                   mundo[i2][i3] = 1
               elif vecinos(l,i2,i3,n,m)==2 and l[i2][i3]==1:
                   mundo[i2][i3] = 1
               else:
                   mundo[i2][i3] = 0
        l=mundo.tolist()
    return l
                   
def vecinos(mundo,x,y,n,m):
    resultado = 0
    if x>0 and y>0 and mundo[x-1][y-1]==1:
        resultado += 1
    if x>0 and mundo[x-1][y]==1:
        resultado += 1
    if x>0 and y<n-1 and mundo[x-1][y+1]==1 :
        resultado += 1
    if y>0 and mundo[x][y-1]==1:
        resultado += 1
    if y<n-1 and mundo[x][y+1]==1:
        resultado += 1
    if x<m-1 and y>0 and mundo[x+1][y-1]==1 :
        resultado += 1
    if x<m-1 and mundo[x+1][y]==1:
        resultado += 1
    if x<m-1 and y<n-1 and mundo[x+1][y+1]==1:
        resultado += 1
    return resultado