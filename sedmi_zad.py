# -*- encoding: utf-8 -*-
import sys
import numpy as np
import re
from collections import Counter

g_lista = []

def count_size_2d_array(ma):
    x = np.array(mat)
    a = np.shape(x)
    a = str(a)
    result = re.findall(r'\d+', a)
    str1 = ''.join(result)
    kon = int(str1)
    return kon

def transpose(array):
    array = array[:]  # make copy to avoid changing original
    n = len(array)
    for i, row in enumerate(array):
        array[i] = row + [None for _ in range(n - len(row))]

    array = zip(*array)

    for i, row in enumerate(array):
        array[i] = [elem for elem in row if elem is not None]

    return array

def convert_np(mat):
    x = np.array(mat)
    return x

def split_2d_ar(array,shap):
    return np.split(array, shap)

def count_consusetive_characters_example(word):
    count=1
    temp_uz = ""
    temp_count = ""
    word = str(word)
    if len(word)>1:
        t = 0
        for i in range(1,len(word)):
           if word[i-1]==word[i]:
              count+=1
           else :
               temp_uz += word[i-1]
               temp_count +=str(count)
               count=1
    else:
        i=0
        temp_uz += word[i-1]
        temp_count +=str(count)
    return (temp_uz)

def count_consusetive_characters_COUNT(word):
    count=1
    temp_uz = ""
    temp_count = ""
    word = str(word)
    if len(word)>1:
        t = 0
        for i in range(1,len(word)):
           if word[i-1]==word[i]:
              count+=1
           else :
               #length += word[i-1]+" repeats "+str(count)+", "
               temp_uz += word[i-1]
               temp_count +=str(count)
               count=1
    else:
        i=0
        temp_uz += word[i-1]
        temp_count +=str(count)
    return (temp_count)

def transposed(seqbag):
    zip(*seqbag)
    map(lambda *row: list(row), *seqbag)
    return map(lambda *row: [elem or 0 for elem in row], *seqbag)

def delite_zeros(t):
    i=0 #loop counter
    length = len(t)  #list length
    while(i<length):
    	if(t[i]==0):
    		t.remove (t[i])
    		length = length -1
    		continue
    	i = i+1
    return t



# print(mat)
# print("transpose of mat :",transpose(mat))


# count = count_size_2d_array(mat)
# mat_T = transposed(mat)

#print(mat_T)
# np_mat_T = convert_np(mat_T)
# temorary = [0]*6

def function_delite_row(matrx):
    np_mat_T = convert_np(matrx)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        #print(np_mat_T[i])
        a = np_mat_T[i]
        t = a.tolist()
        t = delite_zeros(t)
        te = convert_np(t)
        list1.append(te)

    list_t = []
    list_test = []
    spremac = 0
    for i in range(0,len(list1),1):
        a_word = list1[i]
        a = list1[i]
        te = list(a)
        list_t.append(te)

        a = str(a_word).strip('[]')
        a1 = a.replace(', ', '')
        a1 = a.replace(' ', '')
        testni = a1


        temp_count = count_consusetive_characters_COUNT(a1)
        temp_example =count_consusetive_characters_example(a1)
        #print("temp_count",temp_count,"temp_example",temp_example)
        count = 1
        for j in list(temp_count):
            if int(j) > 2 :
                #print(temp_example)
                for t in list_t :
                    cnt = 0
                    if t != g_lista:
                        spremac = i
                        print("t",t,"spremac",g_lista)
                    cnt +=1

                # print("str",str(j),j)
                # for i in range(0,len(g_lista),1):
                #     if g_lista[i] != list_t[spremac]:
                #         print("list_t[spremac]",list_t[spremac])


    g_lista.append(list_t[spremac])
    print("testtiranje : ",type(g_lista))
    #del list_t[spremac]
    return list_t



















mat = [[1,3,2,3,3,1],
       [1,1,3,3,3,1],
       [4,5,5,5,5,1],
       [1,1,2,4,2,5],
       [1,8,2,8,8,2],
       [8,2,3,1,1,2]]

A =   [[1,1,3,3,3,1],
       [4,5,5,5,5,1],]

B =   [[1],
       [1],
       [1],
       [5],
       [2],
       [2]]
C = [[0,0,0,0,0,1]
     [1,1,3,3,3,1],
     [4,5,5,5,5,1],
     [0,0,0,0,0,5],
     [0,0,0,0,0,2],
     [0,0,0,0,0,2]]
c = A+B
A_np = convert_np(A)
B_np = convert_np(B)
C = np.concatenate((A, B))
print("A+B",C)



# def printIntersection(A, B) :
#
#     temp_i = ""
#     temp_j = ""
#     M=N=len(A)
#     for i in range(M) :
#         for j in range(N) :
#
#             # print element value for equal
#             # elements else *
#             if (A[i][j] == B[i][j]):
#                 count = 0
#                 if A[i][j] != 0:
#                     print(A[i][j])
#                     temp_i+= str(i)
#                     print("A[i]",i)
#                     print("A[i]",j)
#                     temp_j += str(j)
#
#
#             else :
#                 print("0")
#
#         print()
#     print("temp_i :",temp_i,"temp_j",temp_j)
#
# print(printIntersection(A,B))

# a = function_delite_row(mat)
# a1 = transposed(a)
# b1 = function_delite_row(a1)
# c = transposed(b1)
# c1 = function_delite_row(c)
# d = transposed(c1)
# d1 = function_delite_row(d)
# print("b1 : ",b1)
# print("g_lista",g_lista[1])
