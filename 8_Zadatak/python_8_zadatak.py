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
list2 = floats[1:]

temp_frst = [0
for i in range(n - 1)] + [list2[n - 1]]
for i in range(n - 2, -1, -1):
    temp_frst[i] = min(temp_frst[i + 1], list2[i])
temp_sum = [0
for i in range(n)]
for i in range(n - 2, -1, -1):
    temp_sum[i] = max(temp_sum[i + 1], list2[i] / temp_frst[i + 1])
for i in range(n - 2):
    print(10 / list2[i] * temp_sum[i + 1])
