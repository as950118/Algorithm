import sys
def input(): # 편의를 위하여
	return sys.stdin.readline().strip()

n = int(input())
arr=[]
ret = 0

for i in range(n):
	arr.append([int(input()), i])

arr.sort()

for i in range(n):
	if (arr[i][1]-i)>ret:
		ret = arr[i][1]-i
print(ret+1)
