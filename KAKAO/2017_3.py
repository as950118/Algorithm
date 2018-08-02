import sys
import math
from collections import deque
sys.setrecursionlimit(10000000)

def find(s, vstr):#Find Data in the Cache
    length = len(vstr)
    for i in range(length):
        if vstr[i] == s:
            return i
    return -1

def LRU(n, arr):#CacheSize, Array
    count = 0
    cache = deque()#Cache (Deque is Efficient to Input and Output)
    for i in range(len(arr)):
        arr[i] = arr[i].upper()#String Unity
        m = find(arr[i], cache)

        if m<0:#Cache miss(Data to DOES NOT be referenced exists in the cache)
            count = count + 5
            if len(cache)<n:#Cache is not full
                cache.append(arr[i])
            else:#Cache is full
                if len(cache) != 0:#If Cache Size == 0 => unavailable Remove last(far left)
                    cache.popleft()
                cache.append(arr[i])
        else:#Cache hit(Data to be referenced exists in the cache)
            count = count + 1
            temp = cache[m]
            #Exchange Hit Data(M'st) <=> Latest Data(Far right)
            cache[m] = cache[len(cache)-1]#Latest Data Input the M'st Index
            cache.pop()#Remove cache[m] == Remove Hit Data(Far right)
            cache.append(temp)#Insert Latest == Insert Hit Data(Far right)

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
