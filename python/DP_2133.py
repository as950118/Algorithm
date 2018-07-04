import sys
sys.setrecursionlimit(1000000000)
debug = 1
while debug:
    n = int(input())
    dp = [n]*10001
    '''
    2 = 3
    4 = 3*3 - 2 + 2*5 - 1 = 18
    6 = 3*3*3-2 + 2*(18*3 - 2) =
    8 =
    '''
    debug = 1
