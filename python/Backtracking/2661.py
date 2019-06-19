n = int(input())
arr = "0"

def check(cur):
    for i in range(cur//2):
        if arr[cur-i:cur+1] == arr[cur-1-2*i:cur-i]:
            return 0
    return 1


def backtracking(cur):
    if cur==n+1:
        return 1
    global arr
    for i in range(1,4):
        arr += str(i)
        if check(cur):
            if backtracking(cur+1):
                return 1
        arr = arr[:-1]
    return 0
backtracking(1)
print(arr[1:])
