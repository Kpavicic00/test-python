# -*- encoding: utf-8 -*-
#   ----------------------------------------------------------------------------------
#   10. Zadatak
#   Napravite program koji će za uneseni broj atoma kisika izračunati koliko molekula željezovog (|||) oksida (Fe2O3) može dobiti. Žečjezo je trovalentno te ga imamo u neograničenim kolčinama.
#   Primjer:
#   Unos|Ispis
#   13 4
#   · Koji tip djeljena u Pythonu trebamo koristiti da bismo dobili točan rezultat?
#   · Koji će biti rezultat amo imamo 23 molekule kisika?
#   ----------------------------------------------------------------------------------

br_molekula = input("Molimo unesite broj molekula : ")

ukupno = br_molekula/3
print("Ispis : ",ukupno," molekula !!")
# trebamo korisitit int() jer on zaokruzuje na cjelobrojnu vrijednost npr 12.6 ce zaokruziti na 12

# 23 /3 = 7.67 azokruzuje na cjelobrojnu vrijednost odnosno program ce ispisati 7 molekula
