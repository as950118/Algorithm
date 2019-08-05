n,m=map(int,input().split())
arrs = list()
for i in range(n):
    arrs.append(str(input()))
point = list(map(int,input().split()))

from collections import defaultdict
dic = [{'A':0, 'B':0, 'C':0, 'D':0, 'E':0} for i in range(m)]
for i in range(n):
    for j, elem in enumerate(arrs[i]):
        dic[j][elem] += 1
ret = 0
for i,d in enumerate(dic):
    temp = 0
    for j in d:
        temp = max(temp, d[j])
    ret += (temp*point[i])
print(ret)
