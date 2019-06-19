import sys
input = lambda:sys.stdin.readline().strip()
n,k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
'''
n=300000
k=8
arr = []
for i in range(n):
    arr.append(i%8 + 1)
'''
check = [[] for i in range(k)]
for i in range(n):
    check[arr[i]-1].append(i)
len_arr = []
for i in range(k):
    len_arr.append((len(check[i]),i))
print(len_arr)
len_arr.sort()
print(len_arr)

def func():
    pass

for i in range(k):
    pass
