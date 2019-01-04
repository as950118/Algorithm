import sys

n, l = map(int, input().split())

ret = -1
length = 0

for i in range(l, 101):
	start = (n//i) + (i//2) - i+1
	if start<0:
		continue
	if i%2==1:
		cal = ((start+1)*2 + i-1-1)*((i-1)/2) + start
	else:
		cal = (start*2 + i-1)*(i/2)
	if cal==n:
		ret = start
		length = i
		break
if ret == -1:
	print(-1)
else:
	for i in range(length):
		print(i+ret, end=" ")
