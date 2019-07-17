n,m = map(int, input().split())
if not n%2:
    if m==0:
        print(1)
    elif m<=n//2:
        print(m)
    else:
        print(n//2-(m-n//2))
else:
    if m==0:
        print(1)
    elif m<=(n//2):
        print(m)
    elif m==(n//2)+1:
        print(m-1)
    else:
        print((n//2)+1 -(m-n//2))