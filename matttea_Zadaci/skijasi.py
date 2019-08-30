# -*- encoding: utf-8 -*-
#   ----------------------------------------------------------------------------------
#   skijasi
#   ----------------------------------------------------------------------------------
N = input("\n\t Molimo unesite ukupni broj skijaša : ")
#temp = 0
niz = [0]*N
count = 0
suma = 0.0
count_prosli = 0
prosao_da_ne = ""
for i in range(0,N,1):
    print("Molimo unesite vrijeme  za .",i+1,". skijasa !")
    temp = raw_input("Vrijeme  : ")
    prosao_da_ne = raw_input("Prošao STRIKTNO unesite DA ili NE  : ")
    if prosao_da_ne =="da" or prosao_da_ne =="Da" or prosao_da_ne =="DA":
        count_prosli +=1
        suma += float(temp)
    if prosao_da_ne =="ne" or prosao_da_ne =="NE" or prosao_da_ne =="Ne":
        count +=1
arit = suma/(count_prosli)
print("Prosjecno vrijeme skijasa je :  ",arit,"sekunda, a palo je  ",count,"skijasa !")
