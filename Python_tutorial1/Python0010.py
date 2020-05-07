#coding=utf-8
#author = zhoulonghai
#【Python0010】正整数的因子展开式

a=int(input())
b=str(a)
num=[]
i=1
while i <= a:
    if a%i == 0:
        a = a/i
        num.append(i)
        i = 1
    i+=1
b+='='+str(num[1])
for j in num[2:]:
    b+="*"+str(j)
print(b)