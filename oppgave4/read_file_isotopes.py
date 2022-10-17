# -*- coding: utf-8 -*-
"""Created on <dagens dato>"""
__author__ = "fornavn etternavn"
__email__ = "brukernavn@nmbu.no"


def readFile(dataLabels = [], dataValues = []):
    temp = []
    try:
        f = open("Oxygen.txt", "r")
        for x in f:
            temp.append(x.rstrip("\n").split("\t"))
        f.close()
    except:
        print("Fikk ikke åpnet fil...")
    for index, x in enumerate(temp):
        if index == 0:
            dataLabels.append(temp[index])
        else:
            dataValues.append(temp[index])
    return dataLabels, dataValues

dataInput = readFile()

print(dataInput[0])
print(dataInput[1])
