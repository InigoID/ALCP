# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:41:45 2022

@author: Iñigo Iriondo Delgado
"""

def es_suma_de_k_potencias_n(x,k,n):
    if sumapotencias(x,n,1,k)>0 or x==0:
        return True
    else:
        return False
        
def sumapotencias(x,n,i,k):
    numero = x - pow(i,n)
    if numero<0 or k==0: 
        return 0
    elif numero==0:
        return 1
    else:
        return sumapotencias(numero,n,i+1,k-1) + sumapotencias(x,n,i+1,k) + sumapotencias(numero,n,i,k-1)
    
        