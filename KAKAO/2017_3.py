import sys
import math
from collections import deque
sys.setrecursionlimit(10000000)

def find(s, vstr):#
    length = len(vstr)
    for i in range(length):
        if vstr[i] == s:
            return i
    return -1

def LRU(n, arr):#CacheSize, Array
    count = 0
    strarr = deque()#Efficient to Inut and Output
    for i in range(len(arr)):
        arr[i] = arr[i].upper()#String Unity
        m = find(arr[i], strarr)

        if m<0:
            if len(strarr)<n:
                count += 5
                strarr.append(arr[i])
            else:
                count = count + 5
                if len(strarr) != 0:
                    strarr.popleft()
                strarr.append(arr[i])
        else:
            temp = strarr[m]
            strarr[m] = strarr[len(strarr)-1]
            strarr.pop()
            strarr.append(temp)
            count = count + 1

    print(count)
    return count

arr1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"];
arr2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"];
arr3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"];
arr4 = ["Jeju", "Pangyo", "NewYork", "newyork"];
arr5 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"];
LRU(3,arr1);
LRU(3,arr2);
LRU(2,arr3);
LRU(5,arr3);
LRU(2,arr4);
LRU(0,arr5);
