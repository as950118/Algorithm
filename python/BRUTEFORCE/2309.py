arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()
ret = sum(arr)

def func():
    for i in range(8):
        for j in range(i+1,9):
            if ret-arr[i]-arr[j] == 100:
                return arr[0:i] + arr[i+1:j] + arr[j+1:9]

for i in func():
    print(i)
