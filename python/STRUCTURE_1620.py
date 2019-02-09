import sys
n, m = map(int ,sys.stdin.readline().strip().split())
num = [None for i in range(n)]
name = {}
for i in range(n):
    Input = sys.stdin.readline().strip()
    num[i]= Input
    name[Input] = i
for i in range(m):
    Input = sys.stdin.readline().strip()
    try:
        print(num[int(Input)-1])
    except:
        print(1+name[Input])
