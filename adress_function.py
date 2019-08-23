# -*- encoding: utf-8 -*-
# Napisati funkciju koja će iz stringa u kojem se nalaze podaci o
#osobi razdvojiti podatke i ispisati ih na ekranu. Podaci o osobi
#koji se nalaze u stringu međusobno su odvojeni zarezom. Podaci
#se uvijek nalaze upisani u sljedećem formatu: ime i prezime, ulica
# i kućni broj, poštanski broj i mjesto
# Program na početku od korisnika traži da se unesu podaci o osobi u
#navedenom formatu a na ekranu ispisuje podatke razdvojeno. Obratiti pažnju na
#kućni broj koji se može sastojati od kućnog broja (uvijek broj) i dodatka kućnom broju.
def cut_number(test_string):
    filter(lambda x: x.isdigit(), test_string)

def splitt(word):
    return [char for char in word]
############################################################
############################################################
# a function that checks that the string contains an integer
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
############################################################
############################################################
# function for insert name
def insert_name():
    while True:
        value = raw_input("\n\tPlease insert NAME : ")
        if hasNumbers(value) == False:
            return value
            break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert NAME !!!")
             continue
############################################################
############################################################
# function for insert surname
def insert_SURNAME():
    while True:
        value = raw_input("\n\tPlease insert SURNAME : ")

        if hasNumbers(value) == False:
            return value
            break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert SURNAME !!!")
             continue
############################################################
############################################################
# function for insert STREET
def insert_STREET():
    while True:
        value = raw_input("\n\tPlease insert STREET : ")

        if hasNumbers(value) == False:
            return value
            break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert STREET !!!")
             continue
############################################################
############################################################
# function for insert Addition to the house number
def Addition_to_the_house_number():
    while True:
        value = raw_input("\n\tPlease insert Addition to the house number : ")

        if hasNumbers(value) == False:
            return value
            break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert Addition to the house number !!!")
             continue
############################################################
############################################################
# function for insert PLACE
def insert_PLACET():
    while True:
        value = raw_input("\n\tPlease insert PLACE : ")

        if hasNumbers(value) == False:
            return value
            break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert PLACE !!!")
             continue
############################################################
############################################################
# function for insert number of people
def number_fun():

    while True:
        value = raw_input("\n\tPlease insert number of people : ")
        if value.isdigit() == True:
            value = int(value)
            return value
            break

        elif value.isdigit() != True:
             print("\n\tPlease insert number of people !!!")
             continue
############################################################
############################################################
# function for insert Zip Code
def ZIP_code_fun():

    while True:
        value = raw_input("\n\tPlease insert ZIP CODE : ")
        if value.isdigit() == True:
            value = int(value)
            return value
            break

        elif value.isdigit() != True:
             print("\n\tPlease insert ZIP CODE !!!")
             continue
############################################################
############################################################
# function for insert HOUSE NUMBER
def HOUSE_NUMBER_fun():

    while True:
        value = raw_input("\n\tPlease insert HOUSE NUMBER : ")
        if value.isdigit() == True:
            value = int(value)
            return value
            break

        elif value.isdigit() != True:
             print("\n\tPlease insert HOUSE NUMBER !!!")
             continue
############################################################
############################################################
n = number_fun()
#print("n",n)
array_storage = [0] * n
count = 0
while (n > 0):
    print("Unesite podatke  za ",count+1,". osobu")
    string = ""
    string += insert_name()
    string += " "
    string += insert_SURNAME()
    string += " , "
    string += insert_STREET()
    string += " "
    string += str(HOUSE_NUMBER_fun())
    string += Addition_to_the_house_number()
    string += " , "
    string += str(ZIP_code_fun())
    string += " "
    string += insert_PLACET()
    string += " "
    n -= 1
    array_storage[count] = string
    count +=1
len_temp = len(array_storage)

ime_prez = "Ime i prezime: "
ulica = "Ulica: "
kuc_br = "Kućni broj: "
dod_kuc_broju = "Dodatak kućnom broju: "
postanski_br = "Poštanski broj: "
mjesto = "Mjesto: "
i = 0

for i in  range(0,len_temp,1):
    temp_strin = array_storage[i]
    data = temp_strin.split(" , ")
    pbr_mj = data[2].split(" ")
    ulc_dodatak = data[1]
    tempry = filter(lambda x: x.isdigit(),data[1])
    ulc_dodatak = ulc_dodatak.split(tempry)

    print("\n\t")
    print(ime_prez+data[0])
    print(ulica+ulc_dodatak[0])
    print(kuc_br+tempry)
    print(dod_kuc_broju+ulc_dodatak[1])
    print(postanski_br+pbr_mj[0])
    print(mjesto+pbr_mj[1])
