import sys
sys.setrecursionlimit(1000000000)
from collections import deque
'''
자기자신을 제외한 소수
소수는 1 == 2번이므로 닫힘
짝수갯수는 2 == 닫힘
홀수갯수는 3 == 열림
'''
arr = [1]*(101)
arr[0], arr[1] = -1, 3
arr[2], arr[3] = 1, 1
t = int(input())
def func(i, cur, last):
    #print(cur, arr.index(1, last+1))
    if cur%arr.index(1, last+1) == 0:
        cur = cur/arr.index(1, last+1)
        if arr[i] == 2:
            arr[i] =3
        else:
            arr[i] = 2
    else:
        last = arr.index(1, last+1)
        if last == lastprimenum:
            if arr[i] == 1:
                return 1
            else:
                return 0
    print(i, cur, last, lastprimenum)
    #print(arr)
    func(i, cur, last)

while t:
    ret = 0
    n = int(input())
    lastprimenum = 3
    for i in range(4, n+1):
        j = func(i,i, 0)
        if j ==1:
            lastprimenum = i
            if i==5:
                print("SEXADSASDASDASDASDASD")
        else:
            pass

    ret = 0

    for i in range(1, n+1):
        if arr[i] == 3:
            ret +=1
    print(ret)
    for i in range(0, 90, 10):
        print(arr[i+1:i+11])
'''
    for i in range(4, n+1):
        if i%2 == 0:
            if arr[i%2] % 2 ==0:
                arr[i] = 3
        else:
            for j in range(primenum):
                if i%arr.index(1)==0:
                    if arr[i] == 0:
                        arr[i] = 2

                    elif arr[i] == 1:
                        arr[i] = 2
                        primenum-=1
                    else:
                        arr[i] = 3:

                else:
                    arr[i] = 1
                    primenum+=1
    for i in range(1, n+1):
        if arr[i]%2 ==1:
            ret +=1
    print(ret)
'''
