import sys
import math
import os
import time
import multiprocessing
sys.setrecursionlimit(1000000000)
from collections import deque
'''
파이썬에서는 글로벌 인터프리터 락이라는 개념이 존재한다.
이 떄문에 스레드를 병렬처리하는 것이 불가능하다.
때문에 작업 속도를 올리기 위해서는 멀티 프로세싱을 이용한다.
하지만 순차적으로 해결해야하는 문제에는 적합하지않다.
예를들면 dp같은 문제

'''
multi_process_time_start = time.time()
def Pac2(j):
    sum = 0
    print("{0} {1}".format(os.getpid(), os.getppid()))
    for i in range(j, j+700):
        sum = sum + i
    return sum

num_list = [1, 701, 1401]
if __name__ == "__main__":

    proc = multiprocessing.Pool(processes=3)
    ret = proc.map(Pac2, num_list)
    proc.close()
    proc.join()
    print(ret)
multi_process_time_end = time.time()
print("Multi Process Run time :", (multi_process_time_end - multi_process_time_start))
