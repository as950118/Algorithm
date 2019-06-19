'''
전체 케이스는 col == n//2 를 중심으로 좌우대칭임

ex)
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0

0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0

때문에, col(x)가 n//2 까지만 가능한 케이스를 구한후
*2 해주면 전체 케이스에 대한 정답을 알 수 있음
또한 홀수의 경우에는 n//2 + 1 를 따로 구헤줘야함
홀수의 경우에는 상하 좌우대칭이 의미없으므로 *2 해주지 않음
'''


n = int(input())
check_row = [0 for i in range(n)]
check_leftcross = [0 for i in range(n*2)]
check_rightcross = [0 for i in range(n*2)]
ret = 0

def backtracking(cur):
    if cur==n:
        global ret
        ret += 1
        return 0
    for i in range(n):
        if check_row[i] or check_leftcross[n+cur-i] or check_rightcross[cur+i]:
            continue
        else:
            check_row[i] = 1
            check_leftcross[n+cur-i] = 1
            check_rightcross[cur+i] = 1
            backtracking(cur+1)
            check_row[i] = 0
            check_leftcross[n+cur-i] = 0
            check_rightcross[cur+i] = 0


for i in range(n//2):
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0
ret = ret*2

if n%2: #홀수일경우
    i=n//2
    check_row[i] = 1
    check_leftcross[n-i] = 1
    check_rightcross[i] = 1
    backtracking(1)
    check_row[i] = 0
    check_leftcross[n-i] = 0
    check_rightcross[i] = 0

print(ret)
