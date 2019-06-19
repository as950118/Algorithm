import sys
cur = 0
max = 0
for i in range(4):
    n, m = map(int , sys.stdin.readline().strip().split())
    cur = cur + (m-n)
    if max<cur:
        max=cur
print(max)
