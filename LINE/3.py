import sys

n = int(input())
table1 = {}
for i in range(n):
    temp = list(map(str,input().split()))
    table1[temp[0]] = temp[1:]
    
n = int(input())
table2 = {}
for i in range(n):
    temp = list(map(str,input().split()))
    table2[temp[0]] = temp[1:]

ret = []
for id in table1:
    try:
        ret.append([id]+table1[id] + table2[id])
    except:
        ret.append([id]+table1[id]+["NULL" for i in range(len(table2['id']))])

ret.sort()
for i in (ret[-1]):
    print(i ,end=" ")
print("")
for i in ret[0:-1]:
    for j in i:
        print(j, end=" ")
    print("")
