from random import *
from time import sleep

n = int(input())
if n==1:
    i = 24
    sleep(1.0)
elif n==2:
    i = 5
    sleep(1.0)
elif n==3:
    i = randint(1, 100)
    sleep(1.0)
elif n==4:
    i = randint(1, 100)
    sleep(1.0)
elif n==5:
    i = randint(1, 6)
    i = 2**i
    sleep(1.0)
else:
    i = randint(1, 100)
    sleep(1.0)

print(i)
