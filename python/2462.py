m,n = map(int, input().split())
arr = [[[[] for z in range(2)] for y in range(m)] for x in range(n)]
for x in range(n):
    for y in range(m):
        arr[x][y][0].append((x,y,1))
        arr[x][y][1].append((x,y,0))
        if x<n-1:
            arr[x][y][0].append((x+1,y,0))
            arr[x][y][1].append((x+1,y,0))
        if x>0:
            arr[x][y][0].append((x-1,y,1))
            arr[x][y][1].append((x-1,y,1))
        if y>0:
            arr[x][y][0].append((x,y-1,0))
            arr[x][y][0].append((x,y-1,1))
        if y<m-1:
            arr[x][y][1].append((x,y+1,0))
            arr[x][y][1].append((x,y+1,1))
for x in range(n):
    for y in range(m):
        print(arr[x][y])
def func(x,y,z, dis):
    if x,y,z == goal_x, goal_y, goal_z:
        return dis
