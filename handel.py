# -*- coding: utf-8 -*- 
"""Created on Sat Sep 17 11:00:00 2022"""
__author__ = "Maria Nybo"
__email__ = "brukenavn@nmbu.no"

#Funksjon for å "vaske" input slik at det kun er mulig å registrere tall
def check_antall():
    while True:
        try:
            antall = float(input("Antall: "))
            break
        except:
            print('Du må angi ett tall for "Antall".')
    return antall

#Funksjon for å "vaske" input slik at det kun er mulig å registrere tall
def check_stykkpris():
    while True:
        try:
            stykkpris = float(input("Pris: "))
            break
        except:
            print('Du må angi ett tall for "Pris".')
    return stykkpris

#Funksjon for å registrere Vare, antall og prisen per vare.
#Benytter en rekursiv funksjon istedet for å bruke en loop for å legge til så mange varer man skulle ønske
#Funksjonen returnerer en liste med varer
def innlesning(vareliste = []):
    print("Registrer ditt input, registrer blankt for å avslutte.")
    varenavn = input("Vare beskrivelse: ")
    if not varenavn:
        return vareliste
    antall = check_antall()
    stykkpris = check_stykkpris()
    innlest_verdi = tuple((varenavn, antall, stykkpris))
    vareliste.append(innlest_verdi)
    output = innlesning(vareliste)
    return output

#funksjon for å bearbeide utskrift av listen med varer
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

#Kaller på utskrift av liste som blir generert av kall på innlesingsfunksjonen slik at bruker kan registrere varene sine.
utskrift(innlesning())
