import sys
sys.setrecursionlimit(10**9)
x, y = map(int, input().split())

z = (y*100//x)
if z==100:
    print(-1)
else:
    z = z/100
    i = 0
    temp2=0
    def func(a,b):
        global x
        global y
        global i
        if a==9:
            for k in range(0,10):
                i += 1
                x = x+1
                y = y+1
                if ((y)/(x))>= z+0.01:
                    return i
            return i
        elif b==1:
            for k in range(10):
                i = i+10**(9-a)
                x = x+10**(9-a)
                y = y+10**(9-a)
                if ((y)/(x))> z+0.01:
                    return func(a+1,-1)
                #elif ((y)/(x))== z+0.01:
                #    return i
            return i
        else:
            for k in range(10):
                i = i-10**(9-a)
                x = x-10**(9-a)
                y = y-10**(9-a)
                if ((y)/(x))< z+0.01:
                    return func(a+1,1)
                #elif ((y)/(x))== z+0.01:
                #    return i
            return i
    for i in range(10):
        if x//(10**i)==0:
            print(func(i+1,1))
            break
