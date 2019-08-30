# -*- encoding: utf-8 -*-
#   ----------------------------------------------------------------------------------
#   8.Zadatak
#   Napišite program za računanje artimetičke sredine plaća u jednoj kompaniji.
#   Korisnik unosi broj zaposlenika, a zatim plaću za svakog od zaposlenika.
#    Program treba ispisati artimetičku sredinu svih plaća i najveću plaću u kompaniji.
#   Primjer:
#   Unos | Ispis
#   4 | Artimetička sredina plaća 362,4 kn, a najveća plaća je 542,1 kn
#   300
#   244
#   123,4
#   542,1
#   ----------------------------------------------------------------------------------

N = input("\n\t Molimo unesite broj zaposlenika u vasoj tvrtci ")
#temp = 0
niz = [0]*N
suma = 0
for i in range(0,N,1):
    print("Molimo unesite placu za .",i+1,". zaposlenika !")
    temp = raw_input("Iznos : ")
    niz[i] = float(temp)
    suma += float(temp)

arit = suma/N
print("Artimeticka sredina place ",arit,"najveca placa je",max(niz))
