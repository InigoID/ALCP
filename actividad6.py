# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 20:36:14 2022

@author: Iñigo Iriondo Delgado
"""

def f(n,m):
    l = pow(7,n,4*10**(m-1))
    return pow(3,l,10**m)

    