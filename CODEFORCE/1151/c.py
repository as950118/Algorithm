import math

MOD = 10**9 + 7
l, r = map(int, input().split())
val = 1<<60
i=0
while 1:
    if r & val:
        val_r = 60-i
        j=0
        while 1:
            if l & val:
                val_l = val_r - j
                break
            val = val>>1
            j += 1
        break
    val = val>>1
    i += 1
arr_t = 6
arr_f = 1
arr = [1, 6]
arr_start = [1, 2]
for i in range(2, val_r+1):
    if i%2:
        arr_t = arr_t*2 + 2
        arr_f = arr_f*2
        arr.append((arr_t)*(arr_f))
        arr_start.append((arr_start[-1]*2))
    else:
        arr_t = arr_t*2
        arr_f = arr_f*2
        arr.append((arr_t)*(arr_f))
        arr_start.append((arr_start[-1]*2-1))
ret = sum(arr[val_l:val_r])
start = arr_start[val_l]
dif = l - (1<<val_l)
if not dif%2:
    ret -= dif//2 * (start + (start+2*(dif-1)))
else:
    ret -= dif//2 * (start + (start+2*(dif-1)))
    ret -= (start + 2*( (dif)//2) )
start = arr_start[val_r]
dif = r - (1<<val_r)
if not dif%2:
    ret += (dif+1)//2 * (start+(start+2*dif))
    ret += start + 2*((dif+1)//2)
else:
    ret += (dif+1)//2 * (start + (start+2*(dif)))
print(ret%MOD)
