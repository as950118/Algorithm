import sys
def input(): #편의를 위해서 정의
	return sys.stdin.readline().strip()
def input_map(): #편의를 위해서 정의
	return map(int, sys.stdin.readline().strip().split())


n = int(input())
a = list(input_map())
b = list(input_map())
ret = 0

for T in range(n):
	max_a = max(a)
	min_b = min(b)
	ret += max_a*min_b
	a.remove(max_a)
	b.remove(min_b)

print(ret)
