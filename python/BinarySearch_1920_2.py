import sys
n = sys.stdin.readline().strip()
arr1 = list(map(int, sys.stdin.readline().strip().split()))
m = sys.stdin.readline().strip()
for i in list(map(int, sys.stdin.readline().strip().split())):
    print(1 if i in arr1 else 0)
