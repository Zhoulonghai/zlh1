#coding=utf-8
#author = zhoulonghai
#【Python0004】验证6174猜想
def Min_Number(a):
    a = str(a)
    arr = []
    for i in range(0,4):
     arr.append(a[i])
    arr.sort()
    return int(''.join(arr))
def Max_Number(a):
    a = str(a)
    arr = []
    for i in range(0, 4):
        arr.append(a[i])
    arr.sort(reverse=True)
    return int(''.join(arr))
a = input()
print(a,end=' ')
while (int(a) != 6174):
    a = Max_Number(a) - Min_Number(a)
    print(a , end=" ")