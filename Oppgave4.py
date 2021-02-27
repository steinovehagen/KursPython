# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:14:34 2020

@author: stein

Kurs i Python Oppgave 4
"""

from math import sin, pi

side1 = float(input("Tast inn side 1: "))
side2 = float(input("Tast inn side 2: "))
vinkel = float(input("Tast inn vinkelen (i grader): "))
vinkel = vinkel*2*pi/360
areal = 1/2*side1*side2*sin(vinkel)

print(areal)