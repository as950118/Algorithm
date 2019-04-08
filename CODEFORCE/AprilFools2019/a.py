n = int(input())
arr = list(map(int,input().split()))
def func(temp_arr):
    if temp_arr == sorted(temp_arr):
        return len(temp_arr)
    return max(func(temp_arr[:len(temp_arr)//2]), func(temp_arr[len(temp_arr)//2:]))

print(func(arr))
