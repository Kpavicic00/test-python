# -*- encoding: utf-8 -*-

# enter the number of rounds
def fun_number_of_rounds():
    while True:
        N = raw_input("  Enter the number of rounds :")

        if N.isdigit() == True:
            N = int(N)
            return N
        else:
             print("\n\t Please input Number !!")
             continue
#################################################################################


# def fun_Input_matches():
#     #N = fun_number_of_rounds()
#     home_goals = 0
#     guest_golas = 0
#
#     number_of_ponts = 0
#     while
