# -*- encoding: utf-8 -*-
#   ----------------------------------------------------------------------------------
#   9. Zadatak
#   Napišite program koji će ispisati broj položenih kolegija nekog studenta. Korisnik unosi broj kolegija koji je student upisao, zatim ocjenu za svaki kolegij. Program treba ispisati koliko je kolegija student položio?
#   Unos|Ispis
#   4 | Student je položio 3 od 4 kolegija
#   5
#   3
#   5
#   1
#   ----------------------------------------------------------------------------------

N = input("\n\t Molimo unesite ukupni broj kolegija : ")
#temp = 0
niz = [0]*N
count = 0
for i in range(0,N,1):
    print("Molimo unesite ocjenu za .",i+1,". kolegij !")
    temp = raw_input("Ocjena : ")
    if int(temp) > 1:
        print("veci")
        count +=1

print("Student je polozio ",count,"od ",N,"kolegija !")
