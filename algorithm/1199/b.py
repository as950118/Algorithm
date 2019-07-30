import math
h,l = map(int, input().split())
'''
l**2 + x**2 = (h+x)**2 = h**2+2*h*x+x**2
x*2*h = l**2-h**2
x = (l**2-h**2)/2*h
'''
print((l**2)/(2*h)-(h**2)/(2*h))
