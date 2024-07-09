A, B, K = map(int, input().split())
g_dic = dict()

def func(n, k):
    if n in g_dic:
        while not n in dic:
            dic[n] = g_dic[n]
            n = g_dic[n]
    if not n in g_dic:
        ret = sum(int(i) ** k for i in str(n))
        dic[n] = ret
        g_dic[n] = ret
        func(ret, k)
    return min(dic)

ret = 0
for n in range(A, B+1):
    dic = dict()
    ret += func(n, K)
print(ret)
    
