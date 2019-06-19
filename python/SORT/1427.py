n = list(str(input()))
arr = []
for i in n:
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    print(i,end="")
