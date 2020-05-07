#coding=utf-8
#author = zhoulonghai
#【Python0003】蒙特·卡罗法计算圆周率
import random
#使用扩展库 random
num=int(input())
ok=0
for i in range(1,num+1):
    x = random.uniform(-1,1)#到-1到1的随机数
    y = random.uniform(-1,1)
    if(x*x+y*y<=1):
        ok+=1
print(ok/num*4)