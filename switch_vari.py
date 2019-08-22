# -*- encoding: utf-8 -*-

def switch_fun(var1,var2):

    # input number for switch
    var1 = input("Input frst number : ")
    var2 = input("Input second number : ")
    print("Before Swapping: x =", var1, " y =", var2)
    var1 = var1 + var2
    var2 = var1 - var2
    var1 = var1 - var2
    print("After Swapping: x =", var1, " y =", var2);
a=0
b=0
switch_fun(a,b)
