def __main__():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    def func(flag, cur, arr):
