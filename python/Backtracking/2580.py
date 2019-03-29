import sys
input = lambda:sys.stdin.readline().strip()
arr = [list(map(int, input().split())) for i in range(9)]
zero = [(x,y) for y in range(9) for x in range(9) if arr[y][x] == 0]
n = len(zero)
available_row = [1022 for i in range(9)]
available_col = [1022 for i in range(9)]
available_box = [[1022 for i in range(3)] for ii in range(3)]
for y in range(9):
    for x in range(9):
        val = 1<<arr[y][x]
        available_row[y] ^= val
        available_col[x] ^= val
        available_box[y//3][x//3] ^= val

def backtracking(cur):
    if cur == n: #n은 zero의 개수
        return 1
    x, y = zero[cur]
    box_x, box_y = x//3, y//3
    available_bit = available_row[y] & available_col[x] & available_box[box_y][box_x]
    len_bit = len(str(bin(available_bit))) - 2
    for i in range(1,len_bit):
        val = 1<<i
        if available_bit & val:
            arr[y][x] = i
            available_row[y] ^= val
            available_col[x] ^= val
            available_box[box_y][box_x] ^= val
            if backtracking(cur+1):
                return 1
            available_row[y] |= val
            available_col[x] |= val
            available_box[box_y][box_x] |= val
    return 0

backtracking(0)
for i in range(9):
    for j in range(9):
        print(arr[i][j], end=" ")
    print("")
