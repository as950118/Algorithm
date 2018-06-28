import sys
sys.setrecursionlimit(1000000000)

n, m = input().split()

n = int(n)
m = int(m)
print(n*m-1)
'''
11 = 0
21 = 1
22 = 3
32 = 5
33 = 8
42 = 7
43 = 11
44 = 15
'''
