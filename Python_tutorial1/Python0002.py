#coding=utf-8
#author = zhoulonghai
#【Python0002】排列组合序列
import itertools #Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
num = input().split( ) #输入n和m
m = int(num[1])
arr = input().split( ) #输入n个字母
#permutations和combinations都是得到一个迭代器
com = list(itertools.combinations(arr,m)) #combinations方法重点在组合
per = list(itertools.permutations(arr,m)) #permutations方法重在排列
print("Permutation:" )
for i in per:
  for j in i:
      print(j , end=" ")
  print()
print("Combination:" )
for i in com:
  for j in i:
      print(j , end=" ")
  print()