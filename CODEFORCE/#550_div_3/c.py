def func():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    set_arr = set(arr)
    temp = [0 for i in range(arr[-1] + 1)]
    for i in arr:
        temp[i] += 1
    for i in temp:
        if i > 2:
            print('No')
            return 0
    inc = [i for i in range(arr[-1] + 1) if temp[i]>1]
    dec = [i for i in range(arr[-1],-1,-1) if temp[i]]
    print('Yes')
    print(len(inc))
    for i in inc:
        print(i, end=" ")
    print("")
    print(len(dec))
    for i in dec:
        print(i, end=" ")
func()
