# -*- encoding: utf-8 -*-

def find_number(list):
    while True:
        value = raw_input("\n\tPlease insert number: ")
        if value == 'x' or value == 'X':
            print("\n Main meni !!")
            break
        if value.isdigit() == True:
            value = int(value)
            count = 0
            if 0 < value  <101:
                for i in range(0,len(list),1):
                    if int(list[i]) == value:
                        count +=1
                        print("pozicija ",list[i]," broja u listi =>",i)

                if count == 0:
                    print("broj ne postoji u listi !!!")

                break
            else:
                print("\n\tPlease insert number between 1 and 100 !!!")
                continue

        elif value.isdigit() != True:
             print("\n\tPlease insert number between 1 and 100 !!!")
             continue

def insert_number(list):
    while True:
        value = raw_input("\n\tPlease insert number between 1 and 100 : ")
        if value == 'x' or value == 'X':
            print("\n Main meni !!")
            break
        if value.isdigit() == True:
            value = int(value)
            if 0 < value  <101:
                list.append(value)
                break
            else:
                print("\n\tPlease insert number between 1 and 100 !!!")
                continue


        elif value.isdigit() != True:
             print("\n\tPlease insert number between 1 and 100 !!!")
             continue

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def meni():
    print("\n\t a) unos/dodavanje novog broja u listu ")
    print("\t b) ispitati koja je pozicija nekog broja u listi ")
    print("\t c) izlaz iz programa !!")

list = []
def insert_option():
    while True:
        meni()
        value = raw_input("\n\tPlease insert option : ")

        if hasNumbers(value) == False:
            ivalue = str(value)
            if value == 'a':
                insert_number(list)
                print(list)
            elif value == 'b':
                find_number(list)
                print(list)
            elif value == 'c':
                print("End of program!!")
                break

        elif hasNumbers(value) == True:
             print("\n\tPlease insert valid option !!!")
             continue
             
#######################
insert_option()
