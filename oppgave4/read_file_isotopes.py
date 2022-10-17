# -*- coding: utf-8 -*-
"""Created on <dagens dato>"""
__author__ = "fornavn etternavn"
__email__ = "brukernavn@nmbu.no"


dataInput = []

def readFile():
    try:
        f = open("Oxygen.txt", "r")
        for x in f:
            temp = x.split("\t")
            dataInput.append(temp)
        f.close()
    except:
        print("Fikk ikke åpnet fil...")

readFile()
print(dataInput)