# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:41:11 2020

@author: stein

Kurs i Python, Oppgave 17
"""
import numpy as np
from pylab import *

x = np.arange(-1,1,0.05)
y1=np.exp(x)
y2=np.exp(-x)
plot(x,y1, label=r"$e^x$")
plot(x,y2, label=r"$e^{-x}$")
xlim(-1,1)
ylim(0,3)
xlabel("X")
ylabel("Y")
legend()
show()

