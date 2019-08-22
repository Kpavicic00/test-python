# -*- encoding: utf-8 -*-

def func_cut_decimal(decim,number_of_places):

    # insert decimal and number of places parametars
    decim = input("Insert decimal number : ")
    number_of_places = input("Insert number of places : ")

    # cut integer part
    int_part = int(decim)
    # copy number of decimal places in second var "a"
    a = number_of_places
    # cut decimal number and storage in var "temp"
    temp = decim - int(decim)
    # moving a decimal point for as many places as the user entered
    while(number_of_places > 0):
        temp = temp *10
        number_of_places -= 1

    # for whatever decimal number it is, that part is saved in the temporary variable "decimal_modif" and saved as an int
    dec_modifi = int(temp)
    # convert to decimal number, with decimal remainder 0
    dec_modifi = dec_modifi/1.0
    # calculates the number of decimals by which it is rounded to obtain eg 123.0 => 123 in var "base"
    base = 10 ** a

    # decimal part ,obtain eg 123 change to 0.123
    decimal_part = dec_modifi / base
    union = int_part + decimal_part
    return union

a = 0
b = 0
k = func_cut_decimal(a,b)
print(k)
