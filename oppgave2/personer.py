# -*- coding: utf-8 -*-
"""Created on Sat Sep 17 11:00:00 2022"""
__author__ = "Navn Navnesen"
__email__ = "brukenavn@nmbu.no"

# Dataentries
nameDB = [
    ['Tore', 'Hansen'],
    ['Silje', 'Olavsen'],
    ['Aase', 'Lund'],
    ['Jens Petter', 'Oremo'],
    ['Tina', 'Kittelsen'],
    ['Dag', 'Paulsen'],
    ['Lena', 'Nilsen'],
    ['Karsten', 'Woll'],
    ['Ine', 'Ørstad'],
    ['Ravn', 'Havnås'],
    ['Jesper', 'Danberg'],
]

# Del 1
def name_check(first, family):
    if first[0] == "T" or family.__len__() > 6 or (first == "Ravn" and family == "Havnås"):
        return True
    return False
for index, name in enumerate(nameDB, start=1):
    if name_check(name[0], name[1]):
        print(str(index) + " " + name[0] + " " + name[1])
