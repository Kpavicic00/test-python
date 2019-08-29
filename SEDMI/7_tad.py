#-*- encoding: utf-8 -*-
import sys
import numpy as np
import re

fullpath = "/home/kristijan/python_test-programi/SEDMI/matrica_txt.txt"
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

mat = [[6,6],
       [1,3,2,3,3,1],
       [1,1,3,3,3,1],
       [4,5,5,5,5,1],
       [1,1,2,4,2,5],
       [1,8,2,8,8,2],
       [8,2,3,1,1,2]]

count = count_size_2d_array(mat)
mat_T = transposed(mat)
np_mat_T = convert_np(mat_T)
temorary = [0]*6
print("temorary",temorary)
print("np_mat_T",np_mat_T)
list1 = []
for i in range(0,len(np_mat_T),1):
    print(np_mat_T[i])
    a = np_mat_T[i]
    print("a = np_mat_T[i]",a,np_mat_T[i] )
    t = a.tolist()
    t = delite_zeros(t)
    te = convert_np(t)
    list1.append(te)

print("konacno",list1)
list_t = []
for i in range(0,len(list1),1):
    a = count_consusetive_characters_COUNT(list1[0])
    b = count_consusetive_characters_example(list1[0])
    print("a : ",a,"\n b : ",b)
#word = [1,2,3,4,5,5,5,5,2,3]
word = "1234555523"
temp_count = count_consusetive_characters_COUNT(word)
temp_example = count_consusetive_characters_example(word)
print("temp_count : ",temp_count)
print("temp_example : ",temp_example)
print("type",type(temp_example))
# for i in temp_count:
#     if int(i)> 2:
#         print(i)
for i in range(0,len(temp_count),1):
    if int(temp_count[i])> 2:
        print("temp_example[i]",temp_example[i],"temp_count[i]",temp_count[i])
