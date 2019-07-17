from collections import deque, defaultdict
n = int(input())
arr = deque((map(int, input().split())))
dp = defaultdict(lambda:-1)
ret = 0
ret_move = ""
test = [0]
def func(arr, cur, val, move):
    if not arr or not arr[0]>cur and not arr[-1]>cur:
        global ret
        global ret_move
        if ret<val:
            ret = val
            ret_move = move
        return 0
    if dp[move] != -1:
        return dp[move]
    dp[move] = 0
    if arr[0]>cur:
        temp = arr.popleft()
        func(arr, temp, val+1, move+"L")
        arr.appendleft(temp)
        dp[move] = ret
    if arr[-1]>cur:
        temp = arr.pop()
        func(arr, temp, val+1, move+"R")
        arr.append(temp)
        dp[move] = ret
    return dp[move]
print(func(arr,0,0,""))
print(ret_move)
