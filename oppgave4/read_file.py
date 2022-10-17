# -*- coding: utf-8 -*-
"""Created on <dagens dato>"""
__author__ = "fornavn etternavn"
__email__ = "brukernavn@nmbu.no"

f = open("Oxygen.txt", "r")
f.readline()
mm = 0
for x in f:
    n = x.split()
    mm += float(n[1])*float(n[2])
f.close()
print(f'Molar masse for isotopene er: {mm:.4f} g/mol')
