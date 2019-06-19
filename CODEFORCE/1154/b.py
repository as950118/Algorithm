import sys

n = int(input())
t = [0 for i in range(101)]
a = []
for i in list(map(int, input().split())):
    if not t[i]:
        t[i] = 1
        a.append(i)
if (max(a) - min(a)) %2:
    if len(a) > 2:
        print(-1)
    else:
        print(max(a) - min(a))
else:
    if len(a) > 2:
        if sum(a) - max(a) - min(a) == min(a) + (max(a)-min(a))//2:
            print(((max(a)-min(a))//2))
        else:
            print(-1)
    else:
        print((max(a)-min(a))//2)
