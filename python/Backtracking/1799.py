import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

one_odd = [(x,y) for y in range(n) for x in range(n) if arr[y][x]==1 and (y+x)%2]
one_even = [(x,y) for y in range(n) for x in range(n) if arr[y][x]==1 and not (y+x)%2]
len_odd = len(one_odd)
len_even = len(one_even)

check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]

def backtracking(cur,val):
    if cur==len_one:
        global ret
        ret = max(ret,val)
        return 0
    x,y = one[cur]
    if check_leftcross[n-y+x] or check_rightcross[y+x]:
        backtracking(cur+1, val)
    else:
        check_leftcross[n-y+x] = 1
        check_rightcross[y+x] = 1
        backtracking(cur+1, val+1)
        #초기화
        check_leftcross[n-y+x] = 0
        check_rightcross[y+x] = 0
        backtracking(cur+1, val)

one = one_odd[:]
len_one = len(one)
ret = 0
backtracking(0,0)
result = ret

one = one_even[:]
len_one = len(one)
ret = 0
backtracking(0,0)
result += ret
print(result)
