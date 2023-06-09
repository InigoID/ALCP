# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 00:23:29 2022

@author: Iñigo Iriondo Delgado
"""

from natural import multiplicar_karatsuba, sumar

def base2_a_decimal_lento(a):
    suma = 0
    for i in range(len(a)):
        suma += a[i]*(2**i)
    return lista(suma)

def base2_a_decimal(a):
    if len(a)<10:
        b = base2_a_decimal_lento(a)
    else:
        b = sumar(base2_a_decimal(a[:len(a)//2]),multiplicar_karatsuba(base2_a_decimal(a[len(a)//2:]),lista(2**(len(a)//2))))
    return b
   
def lista(n):
    lista = []
    while n != 0:
        lista.append(n%10)
        n //= 10
    return lista
