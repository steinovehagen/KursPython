# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:57:57 2020

@author: stein

Kurs i Python Bonusoppgave 10
"""
from math import pi

n=3.5 #viskositeten
r = float(input("Tast inn radius (r): "))
p1 = float(input("Tast inn trykk ved start (p1): "))
p2 = float(input("Tast inn trykk ved slutt (p2): "))
L = float(input("Tast inn lengden (L): "))

qv=pi*r**4*(p1-p2)/(8*n*L)

print(f"Volumstrømmen blir {qv} mm^2/S")

