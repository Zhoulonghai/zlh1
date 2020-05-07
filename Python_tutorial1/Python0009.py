#coding=utf-8
#author = zhoulonghai
#【Python0009】查找鞍点

list1=[]
list_max=[]
list_min=[]
for i in range(5):
    list=input().split()
    list_int=[int(x) for x in list]
    list1.append(list_int )
    k=0
    for j in list_int:
        if j==max(list_int):
            break
        k=k+1
    list_max.append([i+1,k+1, max(list_int)])
#print(list_max)
list2=[[list1[j][i] for j in range(5)] for i  in range(5)]
i=0
for l in list2:
    i=i+1
    k = 0
    for j in l  :
        if j == min(l):
            break
        k = k + 1
    list_min.append([ k + 1,i, min(l)])
#print(list_min)

for i in list_max:
    for j in list_min:
        if str(i)==str(j):
            print(i,end=" ")