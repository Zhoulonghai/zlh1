#coding=utf-8
#author = zhoulonghai
#【Python0005】模拟页面调度LRU算法
def LRU(pages, maxNum, n):
    temp = []
    times = 0
    for page in lst:
        num = len(temp)
        if num < n: # 有空闲主存块
            temp.append(page)
        elif num == n:  # 没有空闲主存块
            if page in temp:  # 要访问的新页面已在主存块中，处理“主存块”，把最新访问的页面交换到列表尾部
                pos = temp.index(page)
                temp = temp[:pos] + temp[pos + 1:] + [page]
            else:  # 要访问的新页面不在主存块中，把最早访问的页面踢掉，调入新页面
                temp.pop(0)
                temp.append(page)
                times += 1
    return times
n = int(input())
lst = tuple(input().split(" "))
print(LRU(lst, 3, n))