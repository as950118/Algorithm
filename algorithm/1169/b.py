n,m = map(int,input().split())
arr_n=[0 for i in range(n+1)]
arr_m=[0 for i in range(m+1)]

for i in range(m):
    n,m = map(int, input().split())
    arr_n[n] += 1
    arr_m[m] += 1

check_n = [[] for i in range(n+1)]
check_m = [[] for i in range(m+1)]
for i in range(n+1):
    temp = arr_n[i]
    if temp>1:
        check_n[temp].append(i)
for i in range(m+1):
    temp = arr_m[i]
    if temp>1:
        check_m[temp].append(i)
