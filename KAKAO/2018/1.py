
def func_7(n):
    temp_1 = 0
    temp_2 = 0
    for i in range(5):
        temp_1 += _7_n[i]
        temp_2 = temp_1 + _7_n[i+1]
        if temp_1 == n:
            return _7[i]
        elif temp_1<n and temp_2>=n:
            return _7[i+1]
    return 0
def func_8(n):
    temp_1 = 0
    temp_2 = 0
    for i in range(4):
        temp_1 += _8_n[i]
        temp_2 = temp_1 + _8_n[i+1]
        if temp_1 == n:
            return _8[i]
        elif temp_1<n and temp_2>=n:
            return _8[i+1]

    return 0

t = int(input())

_7 = [500,300,200,50,30,10]
_7_n = [1,2,3,4,5,6]
_8 = [512, 256, 128, 64 ,32,0]
_8_n = [1,2,4,8,16]

ret = 0

for i in range(t):
    #a = b = i
    a, b = map(int, input().split())
    if a==0:
        if b==0:
            ret = 0
        else:
            ret = func_8(b)
    else:
        ret = func_7(a)
        ret += func_8(b)
    ret *= 10000
    print(ret)
