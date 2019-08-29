# -*- encoding: utf-8 -*-
import sys
import numpy as np
import re
import itertools

fullpath = "/home/kristijan/python_test-programi/SEDMI/matrica_txt.txt"
a = np.loadtxt(fullpath)

g_lista = []

def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))
def count_size_2d_array(ma):
    x = np.array(mat)
    a = np.shape(x)
    a = str(a)
    result = re.findall(r'\d+', a)
    str1 = ''.join(result)
    kon = int(str1)
    return kon
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
               temp_uz += word[i-1]
               temp_count +=str(count)
               count=1
    else:
        i=0
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
    		t.remove(t[i])
    		length = length -1
    		continue
    	i = i+1
    return t
def find_row(matrx):
    np_mat_T = transposed(matrx)
    np_mat_T = transposed(np_mat_T)
    np_mat_T = convert_np(np_mat_T)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        t = a.tolist()
        t = delite_zeros(t)
        te = convert_np(t)
        list1.append(te)

    list_t = []
    list_test = []
    spremac = 0
    spremac_indexa = []
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
        for j in range(0,len(temp_count),1):
            if int(temp_count[j])> 2:
                spremac = i
                spremac_indexa.append(i)

    return spremac_indexa
def find_coll(matrx):
    np_mat_T = transposed(matrx)
    np_mat_T = convert_np(np_mat_T)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        t = a.tolist()
        t = delite_zeros(t)
        te = convert_np(t)
        list1.append(te)

    list_t = []
    list_test = []
    spremac = 0
    spremac_indexa = []
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
        for j in range(0,len(temp_count),1):
            if int(temp_count[j])> 2:
                spremac = i
                spremac_indexa.append(i)
    g_lista.append(list_t[spremac])
    return spremac_indexa
def DELITE_ROW_ZEROOOOS(mat_a):
    np_mat_T = convert_np(mat_a)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        #t = a.tolist()
        #t = delite_zeros(t)
        te = convert_np(a)
        list1.append(te)

    list_t = []
    new_array = []
    spremac = ""
    for i in range(0,len(list1),1):
        #a_word = list1[i]
        a = list1[i]
        te = (a)
        list_t.append(te)
        a = str(te).strip('[]')
        a1 = a.replace(', ', '')
        a1 = a.replace(' ', '')
        testni = a1
        list2 = []
        temp_count = count_consusetive_characters_COUNT(a1)
        temp_example =count_consusetive_characters_example(a1)
        for j in range(0,len(temp_example),1):
            if int(temp_example[j]) >0:
                spremac += str(i)

    temo = len(list_t)-1
    spremac = ''.join(ch for ch, _ in itertools.groupby(spremac))
    t = list(spremac)
    list_index = [0]*len(t)

    co = 0
    for i in spremac:
        list_index[co] = int(i)
        co +=1
    az = missing_elements(list_index)
    new_array = []
    a = np.array(list_t)
    a = np.delete(a, (2), axis=0)
    a = np.delete(a, (2), axis=0)
    return a
def DELITE_ROW(mat_a):
    np_mat_T = convert_np(mat_a)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        te = convert_np(a)
        list1.append(te)

    list_t = []
    spremac = 0
    for i in range(0,len(list1),1):
        a = list1[i]
        te = (a)
        list_t.append(te)
        a = str(te).strip('[]')
        a1 = a.replace(', ', '')
        a1 = a.replace(' ', '')
        testni = a1
        list2 = []
        temp_count = count_consusetive_characters_COUNT(a1)
        temp_example =count_consusetive_characters_example(a1)
        for j in range(0,len(temp_count),1):
            if int(temp_count[j]) > 2:
                spremac = i
    i = int(spremac)
    a = np.array(list_t)
    a = np.delete(a, (i), axis=0)
    return a
def DELITE_ROW_final(mat_a):
    np_mat_T = convert_np(mat_a)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        te = convert_np(a)
        list1.append(te)

    list_t = []
    spremac = 0
    for i in range(0,len(list1),1):
        a = list1[i]
        te = (a)
        list_t.append(te)
        a = str(te).strip('[]')
        a1 = a.replace(', ', '')
        a1 = a.replace(' ', '')
        testni = a1
        list2 = []
        temp_count = count_consusetive_characters_COUNT(a1)
        temp_example =count_consusetive_characters_example(a1)
        for j in range(0,len(temp_count),1):
            if int(temp_count[j]) > 2:
                spremac = i
    a = np.array(list_t)
    a = np.delete(a, (1), axis=0)
    return a
def remove_zeros_from_matrix(mat):
    np_mat_T = convert_np(mat)
    list1 = []
    for i in range(0,len(np_mat_T),1):
        a = np_mat_T[i]
        t = a.tolist()
        t = delite_zeros(t)
        te = convert_np(t)
        list1.append(te)
    return list1
###################################################
###################################################


mat = [[6,6],
       [1,3,2,3,3,1],
       [1,1,3,3,3,1],
       [4,5,5,5,5,1],
       [1,1,2,4,2,5],
       [1,8,2,8,8,2],
       [8,2,3,1,1,2]]

def change_repeting_num_zeros(mat):
    n_row =find_row(mat)
    n_coll = find_coll(mat)

    save_row = []
    save_col = []

    for i in n_row:
        a = int(i)
        save_row.append(a)

    for i in n_coll:
        a = int(i)
        save_col.append(a)

    for i in range(0,len(save_row),1):
        t = save_row[i]
        for j in range(0,len(save_col),1):
            count = 0
            while(count<int(save_col[j])):
                mat[t]=np.delete(mat[t], [0], axis=0)
                count+=1

        new_array = []
        for i in range(0,len(mat),1):
            if type(mat[i]) is list:
                new_array.append(mat[i])
            elif type(mat[i]) is not list:
                a = mat[i].tolist()
                new_array.append(a)


    for i in range(0,len(save_row),1):

        t = save_row[i]
        a = new_array[t]
        i = 0
        while(i<int(save_col[0])):
            a.insert(0, 0)
            i +=1
        mat[t] = a


    return mat

a = change_repeting_num_zeros(mat)
tran_a = transposed(a)
new_s = DELITE_ROW(tran_a)
tran_b = transposed(new_s)
brisi = DELITE_ROW_ZEROOOOS(tran_b)
az = remove_zeros_from_matrix(brisi)
temp_2 = transposed(brisi)
a = DELITE_ROW(temp_2)
b = DELITE_ROW(a)
c = transposed(b)
novi_temp = DELITE_ROW_final(c)
c = np.delete(c, (1), axis=0)
c = np.delete(c, (2), axis=0)
x = remove_zeros_from_matrix(c)
print("Pocetak ",mat)
print("Kraj",x)
