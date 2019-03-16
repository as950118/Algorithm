n = int(input())
height = []
for i in range(n):
    height.append(int(input()))

ret = 0

def func(prv,cur):
    global ret
    for i in range(cur+1,n):
        if height[cur] <= height[i]:
            func(cur, i)
            break
    ret = max(ret, cur-prv)

func(0,0)

height.reverse() #앞이 길고 뒤가 짧은경우도 있으므로
func(0,0)

print(ret)
