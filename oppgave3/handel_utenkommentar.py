# -*- coding: utf-8 -*-
"""Created on Sat Sep 17 11:00:00 2022"""
__author__ = "Navn Navnesen"
__email__ = "brukenavn@nmbu.no"

def check_input(type):
    while True:
        try:
            output = float(input(type + ": "))
            break
        except:
            print('Du må angi ett tall for ' + type +'.')
    return output

def innlesning(vareliste = []):
    print("Registrer ditt input, registrer blankt for å avslutte.")
    varenavn = input("Vare beskrivelse: ")
    if not varenavn:
        return vareliste
    antall = check_input("Antall")
    stykkpris = check_input("Pris")
    innlest_verdi = tuple((varenavn, antall, stykkpris))
    vareliste.append(innlest_verdi)
    output = innlesning(vareliste)
    return output

def utskrift(vareliste):
    total_sum = 0
    print("{:<15}{:>15}".format("Beskrivelse", "Linjekost"))
    print("------------------------------")
    for object in vareliste:
        linjekost = object[1]*object[2]
        total_sum += linjekost
        print("{:<15}{:>15}".format(object[0], "{:.2f}".format(linjekost) + " Kr"))
    print("------------------------------")
    print("{:<15}{:>15}".format("Sum", "{:.2f}".format(total_sum) + " Kr"))

utskrift(innlesning())
