from string import ascii_lowercase
alp = list(ascii_lowercase)

def func():
    arr = list(input())
    arr.sort()
    start = alp.index(arr[0])
    for i in range(1,len(arr)):
        if alp.index(arr[i]) != start+i:
            print('No')
            return 0
    print('Yes')

n = int(input())
for i in range(n):
    func()
