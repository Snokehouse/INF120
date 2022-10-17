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
            dataLabels = temp[index]
        else:
            dataValues.append(list(temp[index]))
    utskriftAvFil(dataLabels, dataValues)
    return

def kalkulasjon_av_molarMasse(data):
    output = 0
    for a, b, c in data:
        output += (float(b)*float(c))
    return output

def utskriftAvFil(labels, data):
    a, b, c = labels
    printLine = "| " + str(a) + " | " + str(b) + " | " + str(c) + " |"
    print("________________________________________________")
    print(printLine)
    print("________________________________________________")
    for x in data:
        a, b, c = x
        printLine = "| " + str(a) + "   |     " + str(b) + "   |       " + str(c) + "     |"
        print(printLine)
        print("________________________________________________")

    print("\n\nIsotopens molekulære masse er: " + str(kalkulasjon_av_molarMasse(data)) + "g/mol.\n")

readFile()
