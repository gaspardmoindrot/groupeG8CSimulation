#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:34:33 2021

Comparaison temps de calcul factorisation par des entiers
"""

import math
from math import gcd
import time
#import matplotlib.pyplot as plt
#import numpy as np
#import pylab
#import pandas as pd




def fermat (N):
    if (N <= 1 or N % 2 == 0):
        return (1)
    a=math.ceil(math.sqrt(N))
    b=a*a-N
    while math.sqrt(b)-math.floor(math.sqrt(b))!=0:
        a=a+1
        b=a*a-N
    return (a-math.sqrt(b), a+math.sqrt(b))


def rho(N):
    
    if (N <= 1):
        return (1)
    number, x = N, 2
    bol = True
    cycle =0

    while bol :    
        cycle +=1
        y = x
        for i in range(2 ** cycle):
            x = (x * x + 1) % number
            factor = gcd(x - y, number)
            if factor > 1:
                bol = False
                return(factor, N/factor)
            
def par_division_succesive(N):
    a = []
    if (N <= 1):
        return (1)
    while N % 2 == 0:
        a.append(2)
        N /= 2
    f = 3
    while f * f <= N:
        if N % f == 0:
            a.append(f)
            N /= f
        else:
            f += 2
    if N != 1: 
        a.append(N)
    # Only odd number is possible
    return a
    


    
    

"Attention, la méthode de fermat et la division succesive fonctionnent uniquement lorsque N est impaire"

print("Bonjour, voici la simulation du groupe G8C avec le langage python (evitez d'ecrire des nombres pairs, l'algorithmes de fermat ne marche que pour les nombres impairs)\n")
a = int(input("Donner un premier nombre : "))
b = int(input("Donner un deuxieme nombre : "))
c = int(input("Donner un troisieme nombre : "))
chiffres = [a, b, c]
tempsfermat = []
tempsrho = []
tempsdivsuc = []

for N in chiffres :
    time1 = time.time();
    fermat(N)
    time2 = time.time();
    tempsfermat.append (time2 - time1)
    
    time1 = time.time();
    rho(N)
    time2 = time.time();
    tempsrho.append (time2 - time1)
    
    time1 = time.time();
    par_division_succesive(N)
    time2 = time.time();
    tempsdivsuc.append (time2 - time1)

print("Algorithmes nombre 1 :")
print("Fermat               : \t", tempsfermat[0])
print("Rho                  : \t", tempsrho[0])
print("Division successive  : \t", tempsdivsuc[0])

print("\nAlgorithmes nombre 2 :")
print("Fermat               : ", tempsfermat[1])
print("Rho                  : ", tempsrho[1])
print("Division successive  : ", tempsdivsuc[1])
   
print("\nAlgorithmes nombre 3 :")
print("Fermat               : \t", tempsfermat[2])
print("Rho                  : \t", tempsrho[2])
print("Division successive  : \t", tempsdivsuc[2])
    
#print ("\nfermat", tempsfermat, "\nrho", tempsrho, "\ndiv", tempsdivsuc)
