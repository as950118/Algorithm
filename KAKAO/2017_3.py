import sys
import math
sys.setrecursionlimit(10000000)

cacheSize = int(input())
cities = list(map(str, input().split()))

cache = []*(cacheSize)

def calc_cache(cache, string, cacheSize):
    try:
        if len(cache) > cacheSize:
            if cache.count(string) == 0:
                cache.pop()
                cache[0] += 1
            elif cache.count(string) == 1:
                cache.remove(string)
        else:
            if cache.count(string) == 0:
                cache[0] += 1
        cache.insert(1, string)
    except:
        cache[0] = len(cities)
    finally:
        return cache
