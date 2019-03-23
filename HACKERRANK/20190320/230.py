'''
a b ab bab abbab bababbab abbabbababbab bababbababbabbababbab abbabbababbabbababbababbabbababbab
'''
import sys
sys.setrecursionlimit(10**6)
def pibo(cur, val):
    pibo_str.append(pibo_str[cur-2] + pibo_str[cur-1])
    pibo_num.append(pibo_num[cur-2] + pibo_num[cur-1])
    if val >= n:
        for i in range(val+1):
            if n == pibo_num[cur]-i:
                return pibo_str[cur][pibo_num[cur]-i]
    else:
        return pibo(cur+1, pibo_num[cur-1] + pibo_num[cur-2])


for t in range(int(input())):
    a,b,n = map(str, sys.stdin.readline().strip().split())
    lena = len(a)
    lenb = len(b)
    n = int(n)
    pibo_str = [a,b]
    pibo_num = [lena, lenb]
    print(pibo(2, lena+lenb))
