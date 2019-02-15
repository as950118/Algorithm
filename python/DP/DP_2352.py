import sys
sys.setrecursionlimit(1000000000)
from collections import deque

n = int(sys.stdin.readline())
arr = deque(map(int, sys.stdin.readline().split()))
arr.appendleft(0)

dp = deque([0])

dp.append(arr[1])
ret = 1

def bisect_left(a, x, lo=0, hi=None):
  if lo < 0:
    raise ValueError('lo must be non-negative')
  if hi is None:
    hi = len(a)
  while lo < hi:
    mid = (lo + hi) // 2  ## 찾는 범위의 중간위치를 구해서
    if a[mid] < x : lo = mid + 1  ## 찾는 값이 더 크면 오른쪽 절반으로 범위 축소
    else: hi = mid  ## 크거나 같으면 왼쪽 절반으로 범위 축소.
    ## 이 때, lo == hi 가 되면 찾은 것이고, lo > hi 가 되면 없는 것이다.
  return lo

for i in range(2, n+1):
    if dp[ret]<arr[i]:
        ret += 1
        dp.append(arr[i])
    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(ret)
