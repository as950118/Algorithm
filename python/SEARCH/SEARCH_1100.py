import sys
def input(): # 편의를 위하여
	return sys.stdin.readline().strip()

ret = 0

for i in range(8):
    arr=input()
    for j in range(8):
        if (i+j)%2==0:
            if arr[j]=="F":
                ret +=1
print(ret)
