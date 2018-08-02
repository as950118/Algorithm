import sys
import math
from collections import deque

sys.setrecursionlimit(1000000000)


n, t, m = map(int, input().split())

timetable = list(map(str, input().split()))
for i in range(len(timetable)):
    timetable[i] = int(timetable[i][0:2])*60 + int(timetable[i][3:5])
print(timetable)
