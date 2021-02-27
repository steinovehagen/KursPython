# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:20:20 2020

@author: stein

Kurs i Python, Oppgave 
"""
from pylab import *

def f(x):
    return sin(x**2)

def g(x):
    return x**2+x/5-exp(-x)

x=linspace(0, 1.7, 20)
y1=f(x)
y2=g(x)

figure(figsize=(2,2))
plot(x,y1, 'o-', label = "f(x)")
plot(x,y2, 'o-', label = "g(x)")
plot([1],[0.85],'o', color="brown")
#scatter([1],[0.85],[1000],color="blue")
legend()
grid()
#rcParams.update({"font.size": 22})
show()
    