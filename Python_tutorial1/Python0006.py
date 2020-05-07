#coding=utf-8
#author = zhoulonghai
#【Python0006】爬楼梯
def climb(num):
    if num == 1:
        return 1
    if num == 2:
       return 2
    if num == 3:
        return 4
    else:
        sum = climb(num-1)+climb(num-2)+climb(num-3)
    return sum
print(climb(int(input())))