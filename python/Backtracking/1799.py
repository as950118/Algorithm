n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
one = [(x,y) for y in range(n) for x in range(n) if arr[y][x]==1]
len_one = len(one)
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]
print(one)

def backtracking(cur):
    if cur==len_one:
        return 1
    x,y = one[cur]
    check_leftcross[n+y-x] = 1
    check_rightcross[y+x] = 1
    ret += backtracking(cur+1)
    #초기화
    check_leftcross[n+y-x] = 0
    check_rightcross[y+x] = 0
