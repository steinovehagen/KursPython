# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:03:10 2020

@author: stein

Kurs i Python, Oppgave 
"""
def f(x):
    return x**2+0.3-1

verdier=[0,1,-0.4]
for x in verdier:
    print(f"f({x})={f(x)}")