from collections import defaultdict
import string
import sys
sys.setrecursionlimit(10**6)
INF = sys.maxsize
alp = string.ascii_uppercase
n = int(input())
s = str(input())
ret_s = "ACTG"
dic = defaultdict(lambda:-1)
ret = INF
def func(cur, val):
    if cur==ret_s:
        return val
    if dic[cur] != -1:
        return dic[cur]
    dic[cur] = INF
    for i in range(n):
        aindex = alp.index(cur[i])
        try:
            ret_s.index(cur[i])
        
        if aindex==25:
            if i==n-1:
                dic[cur] = min(dic[cur], func(str(cur[:i]+alp[0]), val+1 ), func( str(cur[:i]+alp[24]), val+1 ))
            else:
                dic[cur] = min(dic[cur], func( str(cur[:i]+alp[0]+cur[i+1:]), val+1), func( str(cur[:i]+alp[24]+cur[i+1:]), val+1 ))
        else:
            if i==n-1:
                dic[cur] = min(dic[cur], func( str(cur[:i]+alp[aindex+1]), val+1 ), func( str(cur[:i]+alp[aindex-1]), val+1 ) )
            else:
                dic[cur] = min(dic[cur], func(str(cur[:i]+alp[aindex+1]+cur[i+1:]), val+1), func(str(cur[:i]+alp[aindex-1]+cur[i+1:]), val+1))
    return dic[cur]
print(func(s, 0))
