import math

n, k = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = float(arr[i])

ret = (0.0)


def func(a):
    temp_ret = 0.0
    temp_sum = (math.fsum(arr[a:a+k]))
    temp_mean = (temp_sum/k)
    for j in range(k):
        temp_ret += (((math.fsum([arr[a+j],-temp_mean]))*((math.fsum([arr[a+j],-temp_mean])))))
    return math.sqrt(temp_ret/k)

for i in range(n-k+1):
    if i==0:
        ret = (func(i))
    elif k==1:
        ret = 0
    else:
        ret = (min(ret, (func(i))))
print(ret)
