# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:27:45 2020

@author: stein

Kurs i Python Oppgave 5
"""
tall1 = float(input("Tast inn et tall: "))
tall2 = float(input("Tast inn et tall: "))

if tall1>tall2:
    print(f"{tall1} er størst")
elif tall2>tall1:
    print(f"{tall2} er størst")
else:
    print(f"{tall1} og {tall2} er like store")
    
