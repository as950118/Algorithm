import sys
sys.setrecursionlimit(1000000000)

n, q = map(int, input().split())
arr_n = [[0]*(2) for i in range(n)]
arr_q = [[0]*(3) for i in range(q)]
map_x = 0
map_y = 0

for i in range(n):
    arr_n[i] = list(map(int, input().split()))
    map_x = max(map_x, abs(arr_n[i][0]))
    map_y = max(map_y, abs(arr_n[i][1]))

_map = [[0]*((map_y)*2 + 1) for i in range((map_x)*2 + 1)]

ret = 0

dir_x = [-1,1,0,0]
dir_y = [0,0,-1,1]

def func(c_x, c_y, cur_hp, boost):
    global ret
    if e_x==c_x and e_y==c_y:
        ret = 1
        return 1
    if _map[c_x][c_y] == 1:
        _map[c_x][c_y] = 0
        func(c_x, c_y, max_hp, 1)
    if cur_hp==0:
        if boost == 1:
            for i in range(map_x+1):
                if i == c_x:
                    pass
                else:
                    func(i, c_y, cur_hp, 0)
                    func(c_x, -i, cur_hp, 0)

            for i in range(map_y+1):
                if i == c_y:
                    pass
                else:
                    func(c_x, i, cur_hp, 0)
                    func(c_x, -i, cur_hp, 0)
        else:
            return 0
    else:
        for i in range(4):
            if c_y+dir_y[i]<=map_x+1 and c_y+dir_y[i]>=0 and c_x+dir_x[i]<=map_x+1 and c_x+dir_x[i]>=0 :
                func(c_x + dir_x[i], c_y + dir_y[i], cur_hp-1, boost)
        if boost == 1:
            for i in range(map_x+1):
                if i == c_x:
                    pass
                else:
                    func(i, c_y, cur_hp, 0)
                    func(-i, c_y, cur_hp, 0)
            for i in range(map_y+1):
                if i == c_y:
                    pass
                else:
                    func(c_x, i, cur_hp, 0)
                    func(c_x, -i, cur_hp, 0)

    return 0
for i in range(q):
    for j in range(n):
        _map[arr_n[j][0]][arr_n[j][1]] = 1

    s, e, max_hp= map(int, input().split())
    s_x, s_y = arr_n[s-1][0]+map_x+1, arr_n[s-1][1]+map_y+1
    e_x, e_y = arr_n[e-1][0]+map_x+1, arr_n[e-1][1]+map_y+1
    ret = 0
    func(s_x, s_y, max_hp, 0)
    if ret:
        print("YES")
    else:
        print("NO")
