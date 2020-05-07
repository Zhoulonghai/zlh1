#coding=utf-8
#author = zhoulonghai
#【Python0011】牛顿迭代法
from math import fabs

def solut(a,b,c,d,e):
    x1=e
    # 迭代:
    while True:
        x=x1
        f = ((a * x + b) * x + c) * x + d #原函数
        f1 = (3 * a * x + 2 * b) * x + c #求导的函数
        x1 = x - f / f1
        if (fabs(x1 - x) <= 0.00000001):
            return x1
num = [float(n) for n in input('').split()]
print(("%0.2f")%(solut(num[0],num[1],num[2],num[3],num[4])))