# -*- encoding: utf-8 -*-
#   ----------------------------------------------------------------------------------
#   11. Zadatak
#   Množinski udio je omjer množine tvari B i zbroja množine svih tvari u toj smjesi.
#   Napravite program koji će za uneseni množinski udio
#   tvari ispisati množinski udio prve tvari i druge tvari.
#   Unos | Ispis
#   12 0.75
#   4 0.25
#   ----------------------------------------------------------------------------------

prva_tvar = input("Molimo unesite kolicinu prve tvari : ")
druga_tvar = input("Molimo unesite kolicinu druge tvari : ")
mnozinski_udio_PRVE_TVARI = prva_tvar/float(prva_tvar+druga_tvar)
mnozinski_udio_DRUGEE_TVARI = druga_tvar/float(prva_tvar+druga_tvar)
print("Mnozinski udio prve tvari : ",mnozinski_udio_PRVE_TVARI)
print("Mnozinski udio druge tvari : ",mnozinski_udio_DRUGEE_TVARI)
