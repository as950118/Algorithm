import sys

x = list(map(int, input().split()))

a_b_c = max(x)
x.remove(a_b_c)
for i in x:
    print(a_b_c - i, end=" ")
