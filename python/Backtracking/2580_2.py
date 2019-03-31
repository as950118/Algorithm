import sys
input = lambda:sys.stdin.readline().strip()

arr = [list(map(int, input().split())) for i in range(9)]
zero = [(x,y) for y in range(9) for x in range(9) if arr[y][x] == 0] #zero를 찾음
n = len(zero) #zero의 개수

available_row = [set(i for i in range(1,10)) for ii in range(9)] #y번째열에서 가능한
available_col = [set(i for i in range(1,10)) for ii in range(9)] #x번째열에서 가능한
available_box = [[set(i for i in range(1,10)) for ii in range(3)] for iii in range(3)] #[y//3] \[x//3] 박스에서 가능한
for y in range(9):
    available_row[y].difference_update(set(arr[y]))
    for x in range(9):
        available_col[x].discard(arr[y][x]) #discard는 key error를 반환하지 않음
        available_box[y//3][x//3].discard(arr[y][x])

def backtracking(cur):
    if cur == n: #n은 zero의 개수
        return 1
    x, y = zero[cur] #x,y
    box_x, box_y = x//3, y//3 #박스 위치
    #x,y열 그리고 [y//3][x//3]박스의 공집합을 구함
    for num in (available_row[y].intersection(available_col[x])).intersection(available_box[box_x][box_y]):
        arr[y][x] = num
        available_row[y].discard(num)
        available_col[x].discard(num)
        available_box[box_y][box_x].discard(num)
        if backtracking(cur+1):
            return 1
        available_row[y].add(num)
        available_col[x].add(num)
        available_box[box_y][box_x].add(num)
    return 0

backtracking(0)
for i in range(9):
    for j in range(9):
        print(arr[i][j], end=" ")
    print("")
