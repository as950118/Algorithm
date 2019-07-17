import sys
sys.setrecursionlimit(10**8)
h = []

n = int(input())
h.append(list(map(int, input().split())))
h.append(list(map(int, input().split())))
visit = [[-1 for i in range(n)] for ii in range(2)]
# n = 100000
# h = [[i for i in range(100000)] for ii in range(2)]
# visit = [[-1 for i in range(100000)] for ii in range(2)]
ret = 0
def func(col, row, count):
    global ret
    next_row = abs(row-1)
    if col==n-1:
        return count
    if col == n-2:
        return count + h[next_row][n-1]
    if visit[row][col] != -1:
        visit[row][col] = max(visit[row][col], count)
        return visit[row][col]
    visit[row][col] = count
    if h[next_row][col+2] > h[next_row][col+1] + h[row][col+2]:
        visit[row][col] = (func(col+2, next_row, count+h[next_row][col+2]))
    else:
        visit[row][col] = (func(col+2, row, count+h[next_row][col+1] + h[row][col+2]))
    return visit[row][col]
if n==1:
    print(max(h[0][0],h[1][0]))
else:
    print(max(func(0,0,h[0][0]), func(0,1,h[1][0])))
