# -*- coding: utf-8 -*-
"""Created on Sat Sep 17 11:00:00 2022"""
__author__ = "Navn Navnesen"
__email__ = "brukenavn@nmbu.no"

# Dataentries
innsamling_hist = [
    [2015, 86343, 123],
    [2016, 93512, 125],
    [2017, 83935, 119],
    [2018, 91274, 128],
    [2019, 88935, 127],
    [2020, 95182, 132],
]

# Del 1
for entry in innsamling_hist:
    print(str(entry[0]) + ": " + str(round(entry[1]/entry[2], 2)) + " kr/bøssebærer")

# Del 2
hoyesteSnittInnsamlet = [0 , 0]

for entry in innsamling_hist:
    snittInnsamlet = round(entry[1]/entry[2], 2)
    if snittInnsamlet > hoyesteSnittInnsamlet[1]:
        hoyesteSnittInnsamlet[0] = entry[0]
        hoyesteSnittInnsamlet[1] = snittInnsamlet

print(
    "\n\n" +
    str(hoyesteSnittInnsamlet[0]) +
    " hadde det høyeste gjennomsnittet per bøssebærer.\nSnittet dette året var: " +
    str(hoyesteSnittInnsamlet[1]) +
    " Kr per Bøssebærer."
    )


"""
a) Svaret er:

2015: 701.98 kr/bøssebærer
2016: 748.1 kr/bøssebærer
2017: 705.34 kr/bøssebærer
2018: 713.08 kr/bøssebærer
2019: 700.28 kr/bøssebærer
2020: 721.08 kr/bøssebærer

b) Svaret er:

2016 hadde det høyeste gjennomsnittet per bøssebærer.
Snittet dette året var: 748.1 Kr per Bøssebærer.

"""