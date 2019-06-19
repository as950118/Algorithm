n = int(input())

arr = [0]*(3)
dp_max = [0]*(3)
dp_min = [0]*(3)

arr = list(map(int, input().split()))
temp = arr[:]
dp_max = temp[:]
dp_min = temp[:]

for i in range(1, n):
    arr = list(map(int, input().split()))
    temp[0] = max(dp_max[0], dp_max[1]) + arr[0]
    temp[1] = max(dp_max[0], dp_max[1], dp_max[2]) + arr[1]
    temp[2] = max(dp_max[1], dp_max[2]) + arr[2]
    dp_max = temp[:]

    temp[0] = min(dp_min[0], dp_min[1]) + arr[0]
    temp[1] = min(dp_min[0], dp_min[1], dp_min[2]) + arr[1]
    temp[2] = min(dp_min[1], dp_min[2]) + arr[2]
    dp_min = temp[:]

print(max(dp_max), min(dp_min))
