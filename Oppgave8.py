# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:51:47 2020

@author: stein

Kurs i Python, Oppgave 8
"""
from numpy import sqrt

print("Tast 2.gradsligningen på formen: ax^2+bx+c=0")
a=float(input("Tast inn a: "))
b=float(input("Tast inn b: "))
c=float(input("Tast inn c: "))

d=b**2-4*a*c

if d>0:
    x1=-b+sqrt(d)/(2*a)
    x2=-b-sqrt(d)/(2*a)
    print(f"{a}x^2+{b}x+c=0 gir løsningene x1 = {x1} og x2 = {x2}")

elif d<0:
    re = -b/(2*a)
    im1 = d/(2*a)
    im2 = -d/(2*a)
    resultat = f"{a}x^2+{b}x+c=0 gir den komplekse løsningen x1 = {re}"
    if(im1>0):
        resultat += " +"
    resultat += f" {im1}i og "
    resultat += f" x2 = {re}"
    if(im2>0):
        resultat += f" +"
    resultat += f"{im2}i"
    print(resultat)
    #print(f"{a}x^2+{b}x+c=0 gir den komplekse løsningen x1 = {re} + {im1}i og x2 = {re} + {im2}i")
 
else:
    x1=-b/(2*a)
    print(f"{a}x^2+{b}x+c=0 gir bare en reell løsning x1 = {x1}") 