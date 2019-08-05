n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
if not n==1:
    arr = arr[n//2:]
    cai = arr[1]-arr[0]
    if not cai>k:
        arr[0] += cai
        k -= cai
    for i in range(k):
        arr[0] += 1
        arr.sort()
    print(arr[0])
else:
    print(arr[0])
