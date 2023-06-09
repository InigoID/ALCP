# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:15:29 2022

@author: Inigo Iriondo Delgado
"""

def eliminar5(n0):
    i = 0
    numero = 0
    if n0<0:
        signo = -1
    else:
        signo = 1
    n = abs(n0)
    while n != 0:
        m = n%10
        if m != 5:
            numero += m*(10**i)
            i += 1
        n //= 10
    return numero*signo