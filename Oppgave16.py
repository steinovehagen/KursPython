# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:14:23 2020

@author: stein

Kurs i Python, Oppgave 
"""

def kanonkule_x(t):
    return 25*t

def kanonkule_y(t):
    return 45*t-5*t**2

def kanonkule_posisjon(t):
    return kanonkule_x(t),kanonkule_y(t)

def kanonkule():
    tid = float(input("Tast inn tiden for kanonkula: "))
    x,y=kanonkule_posisjon(tid)
    print(f"kanonkula har beveget seg {x}m i x-retning og {y}m i y-retning")
    
def kanonkule_bane():
    for t in range(0,10):
        x,y=kanonkule_posisjon(t)
        print(f"t={t}: x={x},y={y}")      
    
#kanonkule()
kanonkule_bane()
