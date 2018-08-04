import sys
import math
sys.setrecursionlimit(1000000000)
from collections import deque

temp = "festival==kakao&&festival==2018&&haha==123456&&hoho!=123456"
arr = deque(map(str, temp.split("&&")))
#arr = deque(map(str, input().split("&&")))
l = len(arr)
arr_var = deque([""]*(1) for i in range(l))
arr_jug = deque([""]*(1) for i in range(l))
arr_val = deque([""]*(1) for i in range(l))
print(arr,"\n",arr_var,"\n",arr_jug,"\n",arr_val)

for i in range(l):
    try:
        arr_var[i][0], arr_val[i][0] = map(str, arr[i].split("=="))
    except:
        arr_var[i][0], arr_val[i][0] = map(str, arr[i].split("!="))
    arr_jug[i][0] = list(map(str, arr[i].split(arr_val[i][0])))[0]
    arr_jug[i][0] = list(map(str, arr_jug[i][0].split(arr_var[i][0])))[1]

print(arr,"\n",arr_var,"\n",arr_jug,"\n",arr_val)
for i in range(len(arr_var)):
    for j in range(len(arr_var)):
        if arr_var[i] == arr_var[j]:
            if len(arr_var[i]) < len(arr_val[i]):
                arr_val[i].append(arr_val[i])
                arr_var.remove(arr_var[i])
                arr_val.remove(arr_val[i])
            else:
                if len(arr_val[i]) < len(arr_val[j]):

                    arr_var[i].append(arr_var[i])
                    arr_var.remove(arr_var[i])
                    arr_val.remove(arr_val[i])
            print(arr,"\n",arr_var,"\n",arr_jug,"\n",arr_val)
