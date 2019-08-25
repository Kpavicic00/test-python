# # -*- encoding: utf-8 -*-
import csv
import numpy as np
prvi_file = "/home/kristijan/python_test-programi/8_Zadatak/prvi_primjer.txt"
drugi_file = "/home/kristijan/python_test-programi/8_Zadatak/drugi_primjer.txt"



with open(drugi_file, 'r') as f:
        data = f.read().split()
        floats = []
        for elem in data:
            try:
                floats.append(float(elem))
            except ValueError:
                pass
        print floats


n = int(floats[0])
print("n",n)
array = [0.0]*n
print("array",array)
print("type",type(floats))
list2 = floats[1:]
print("list2",list2)

#######################

print("array[0]",array[0])
print("array",array)


#list.remove(element)
#n = int(input())

#a = [(list2) for i in range(n)]
a = list2
print(a)
min_desno = [0 for i in range(n - 1)] + [a[n - 1]]
for i in range(n - 2, -1, -1):
 min_desno[i] = min(min_desno[i + 1], a[i])
max_omjer_desno = [0 for i in range(n)]
for i in range(n - 2, -1, -1):
 max_omjer_desno[i] = max(max_omjer_desno[i + 1], a[i] / min_desno[i + 1])
for i in range(n - 2):
 print(10 / a[i] * max_omjer_desno[i + 1])
##########################
# print("array",array,type(array))
# a = [array for i in range(n)]
#
# min_desno = [0 for i in range(n - 1)] + [a[n - 1]]
#
# for i in range(n - 2, -1, -1):
#      min_desno[i] = min(min_desno[i + 1], a[i])
#      max_omjer_desno = [0 for i in range(n)]
#
#
# for i in range(n - 2, -1, -1):
#     max_omjer_desno[i] = max(np.array(max_omjer_desno[i + 1]), a[i] / np.array(min_desno[i + 1]))
#
# for i in range(n - 2):
#     print(10 / a[i] * max_omjer_desno[i + 1])



# n = int(input())
# a = [float(input()) for i in range(n)]
# print("type",type(a),a)
# min_desno = [0 for i in range(n - 1)] + [a[n - 1]]
# for i in range(n - 2, -1, -1):
#  min_desno[i] = min(min_desno[i + 1], a[i])
# max_omjer_desno = [0 for i in range(n)]
# for i in range(n - 2, -1, -1):
#  max_omjer_desno[i] = max(max_omjer_desno[i + 1], a[i] / min_desno[i + 1])
# for i in range(n - 2):
#  print(10 / a[i] * max_omjer_desno[i + 1])
