import sys
sys.setrecursionlimit(1000000000)
debug = 1
dp = [0]*10000001
'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
1 2 3 1 2 3 4 2 1 2  3  3  2  3  4  1  2  2  3  2  3  3
'''
def func(n, i):
    global ret
    while 1:
        if n==i**2:
            ret +=1
            break
        if n>i**2:
            max = n/i**2
            if max:
            func(n, i+1)
            break
        else:
            i+=1
while debug:
    ret=0
    n = int(input())
    print(dp[n])
    debug=1
