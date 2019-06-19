import math

n = int(input())
val = [0 for i in range(10)]
start = 1
ret = 1

while 1:
    if n<start:
        break
    while 1:
        if n%10 == 9 or n<start:
            break
        temp_n = n
        while 1:
            if temp_n <= 0:
                break
            val[temp_n%10] += ret
            temp_n //= 10
        n -= 1

    if n<start:
        break
    while 1:
        if start%10 == 0 or n<start:
            break
        temp_start = start
        while 1:
            if temp_start <= 0:
                break
            val[temp_start%10] += ret
            temp_start //= 10
        start += 1

    n //= 10
    start //= 10

    for i in range(10):
        val[i] += (n-start+1)*ret

    ret *= 10

for i in val:
    print(i, end=" ")
