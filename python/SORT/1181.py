import sys
input = lambda:sys.stdin.readline().strip()

n = int(input())
arr = [set() for i in range(51)]
for i in range(n):
    temp = input()
    arr[len(temp)].add(temp)
for elem in arr:
    if elem:
        for x in sorted(elem):
            print(x)
