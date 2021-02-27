# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:06:03 2020

@author: stein

Kurs i Python, Oppgave 18
"""
from pylab import *

def f(x):
    return x**2-5*x+9

x=linspace(0,5,100)
y=f(x)

print(x,y)


plot(x,y,label = "2.gradsfunksjon")
xlabel("X-verdier")
ylabel("Y-verdier")
legend()
show()