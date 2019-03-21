import sys
input = lambda:sys.stdin.readline()

arr = [0 for i in range(10001)]
for i in range(int(input())):
    arr[int(input())] += 1
for i in range(10001):
    if arr[i]:
        for j in range(arr[i]):
            print(i)
