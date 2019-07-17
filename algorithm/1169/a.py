n, a,x, b,y = map(int, input().split())


def func(A,B, check):
    if A==B and check:
        return 'YES'

    if A==x or b==y:
        return 'NO'

    if A==n:
        A=1
    else:
        A+=1

    if B==1:
        B=n
    else:
        B-=1

    return func(A,B,1)

print(func(a,b,0))