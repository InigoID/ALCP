# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 11:58:09 2022

@author: Iñigo Iriondo Delgado
"""

def f(n):
    resultados = [0]*(n+1)
    for i in range(1,n+1):
        resultados[i] = resultados[i-1] + resultados[i//2] + d(i)
    return resultados[n]

def d(n):
    if n//10 != n/10:
        return n%10
    else:
        return d(n//10)
