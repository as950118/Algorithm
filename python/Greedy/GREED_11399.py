n = int(input())
arr = list(map(int, input().split()))
arr.sort()
ret = 0
for i in range(len(arr)):
    ret += sum(arr[:i+1])
print(ret)
