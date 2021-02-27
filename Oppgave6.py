# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:37:42 2020

@author: stein

Kurs i Python Oppgave 5
"""
tall1 = float(input("Tast inn et tall: "))
tall2 = float(input("Tast inn et tall: "))
abstall1=abs(tall1)
abstall2=abs(tall2)

print(abstall1,abstall2)

if abstall1>abstall2:
    print(f"absoluttverdien til {tall1} er størst")
elif abstall2>abstall1:
    print(f"absoluttverdien til {tall2} er størst")
else:
    print(f"absoluttverdien til {tall1} og {tall2} er like store")