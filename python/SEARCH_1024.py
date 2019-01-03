import sys
sys.setrecursionlimit(1000000)

def input(): # 편의를 위하여
	return sys.stdin.readline().strip()

n, l = map(int, input().split())

def func(start, length, val):
    if length>100 or start<0:
        return -1
    if val==n:
        return start
    if val>n:
        return func(start-1, length, val+start-1-(start-1+length))
    if val<n:
        return func(start-1, length+1, val+start-1)

temp = 0
Start = func((n//l), l, (((n//l)+l-1)*(((n//l)+l))//2) - (((n//l)-1)*((n//l))//2))
if Start == -1:
    print(-1)
else:
    while 1:
        print(Start, end=" ")
        temp += Start
        Start += 1
        if temp==n:
            break
