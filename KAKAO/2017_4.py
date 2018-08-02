import sys
import math
from collections import deque

sys.setrecursionlimit(1000000000)

timetable1 = ["08:00", "08:01", "08:02", "08:03"]
timetable2 = ["09:10", "09:09", "08:00"]
timetable3 = ["09:00","09:00" ,"09:00", "09:00"]
timetable4 = ["00:01", "00:01", "00:01", "00:01", "00:01"]
timetable5 = ["23:59"]
timetable6 = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]

timetable=[timetable1, timetable2, timetable3, timetable4, timetable5, timetable6]
n = [1, 2, 2, 1, 1, 10]
t = [1, 10, 1, 1, 1, 60]
m = [5, 2, 2, 5, 1, 45]

count = [0]*(6)
ret = [0]*(6)

def func(i, min_time, max_time):
    for j in range(len(timetable[i])):
        if min_time<timetable[i][j] and timetable[i][j] <= max_time:
            count[i] += 1

    if count[i]<=m[i]:
        ret[i] = (n[i]-1)*(t[i]) + max_time
    else:
        count[i] -= m[i]
        n[i] -= 1
        func(i, max_time, max_time + m[i])
    print(ret)

for i in range(6):
    for j in range(len(timetable[i])):
        timetable[i][j] = int(timetable[i][j][0:2])*60 + int(timetable[i][j][3:5])

for i in range(6):
    func(i, 0, 540)
print(ret)
