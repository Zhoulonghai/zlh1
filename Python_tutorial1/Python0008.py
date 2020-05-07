# coding=utf-8
# author = zhoulonghai
# 【Python0008】筛法求素数

import numpy
import math
num = [int(n) for n in input('').split()]
MAX_INT = num[1]
MIN_INT = num[0]
marks_bool = [True] * (MAX_INT + 1)
for i in range(2,int(math.sqrt(MAX_INT)) + 1):
    j = i
    k = j
    while j * k <= MAX_INT:
        marks_bool[j * k] = False
        k += 1
sum_int = 0
l = []
for i in range(2,MAX_INT + 1):
    if marks_bool[i] is True:
        if(i >= MIN_INT):
            l.append(i)
km = [num for elem in numpy.array(l).reshape(-1,5) for num in elem]
p = 1
for num in km:
    print(num , " ", end ="")
    if p % 5 == 0 :
        print("")
    p = p + 1