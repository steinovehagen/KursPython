# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 15:24:56 2020

@author: stein

Kurs i Python, Oppgave 
"""
n = int(input("Tast inn et tall: "))
fakultet = 1
for x in range(n,0,-1):
    fakultet*=x
    
print(fakultet)