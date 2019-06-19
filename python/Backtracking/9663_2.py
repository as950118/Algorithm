'''
col, row, left cross, right cross를 체크해줘야함
col(x)를 기준으로 가능한 모든 row(y)을 찾는방식으로 진행함
또한 그 과정에서 대각선을 체크하여 시간을 줄임

ex)
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0

leftcross
0,3 = 0
0,2 1,3 = 1
0,1 1,2 2,3 = 2
0,0 1,1 2,2 3,3 = 3
1,0 2,1 3,2 = 4
2,0 3,1 = 5
3,0 =  6
rigthcross
0,0 = 0
0,1 1,0 = 1
0,2 1,1 2,0 = 2
0,3 1,2 2,1 3,0 = 3
1,3 2,2 3,1 = 4
2,3 3,2 = 5
3,3 = 6
leftcross는 leftcross[n+x-y] 을 체크
rightcross는 rigthcross[x+y] 을 체크
'''


n = int(input())
check_row = [0 for i in range(n)]
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]

def backtracking(cur):
    if cur==n:
        return 1
    ret = 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            ret += backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0
    return ret


print(backtracking(0))
