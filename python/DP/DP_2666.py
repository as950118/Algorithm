import sys
sys.setrecursionlimit(1000000)

_ = int(sys.stdin.readline())#벽장의 개수, 사용하지 않기 때문에 underscore로 처리
x1, x2 = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
	arr.append(int(sys.stdin.readline()))

def func(a1,a2,idx,ret):
	if idx==n:
		return ret
	return min(func(arr[idx], a2, idx+1, ret+abs(a1-arr[idx])),func(a1, arr[idx], idx+1, ret+abs(a2-arr[idx])))
print(func(x1,x2,0,0))
