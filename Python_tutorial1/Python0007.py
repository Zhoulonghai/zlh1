#coding=utf-8
#author = zhoulonghai
#【Python0007】杨辉三角形

def YangHui (num):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j == 0 else LL[i-1][j-1])+ (0 if j == len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL
a = int(input())
for i in YangHui(a+1):
    for j in i:
        print("%5d"%j,end="")
    print()