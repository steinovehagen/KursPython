# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:41:42 2020

@author: stein

Kurs i Python oppgave 7
"""

vinkel = float(input("tast inn vinkel: "))
if vinkel<90:
    print(f"{vinkel} grader er en spiss vinkel")
elif vinkel>90:
    print(f"{vinkel} grader er en stump vinkel")
else:
    print(f"{vinkel} grader er en rett vinkel")