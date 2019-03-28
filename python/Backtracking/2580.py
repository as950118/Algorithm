arr = [[] for i in range(9)]
zero = []
for y in range(9):
    arr[y] = list(map(int, input().split()))
    for x in range(9):
        if arr[y][x] == 0:
            zero.append((x,y))
n = len(zero)
def backtracking(cur):
    if cur == n:
        return 1
    available_num = [i for i in range(1,10)]
    x, y = zero[cur]
    for new in range(9):
        try:
            available_num.remove(arr[y][new])
        except:
            pass
        try:
            available_num.remove(arr[new][x])
        except:
            pass
    for num in available_num:
        arr[y][x] = num
        if backtracking(cur+1):
            return 1
    return 0

backtracking(0)
for i in range(9):
    for j in range(9):
        print(arr[i][j], end=" ")
    print("")
