n = int(input())
arr=list(map(int, input().split()))
for q in range(int(input())):
    temp = list(map(int, input().split()))
    if temp[0]==1:
        arr[temp[1]-1] = temp[2]
    else:
        t = temp[2]
        for i in range(n):
            if arr[i]<t:
                arr[i]=t
for i in range(n):
    print(arr[i], end=" ")
