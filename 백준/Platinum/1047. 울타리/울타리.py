import sys
from itertools import combinations
from functools import cmp_to_key

class Node:
    def __init__(self, x, y, w, idx):
        self.x = x
        self.y = y
        self.w = w
        self.idx = idx

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    trees = []
    vx = []
    vy = []
    
    # 데이터 파싱
    index = 1
    for i in range(N):
        x = int(data[index])
        y = int(data[index + 1])
        w = int(data[index + 2])
        node = Node(x, y, w, i)
        trees.append(node)
        vx.append(node)
        vy.append(node)
        index += 3
    
    # x축, y축 기준으로 정렬
    vx.sort(key=lambda n: (n.x, n.y))
    vy.sort(key=lambda n: (n.y, n.x))
    
    res = float('inf')
    
    # 모든 가능한 직사각형 범위 조합을 확인
    for xi in range(N):
        for xj in range(xi, N):
            for yi in range(N):
                for yj in range(yi, N):
                    minx = min(vx[xi].x, vx[xj].x, vy[yi].x, vy[yj].x)
                    maxx = max(vx[xi].x, vx[xj].x, vy[yi].x, vy[yj].x)
                    miny = min(vx[xi].y, vx[xj].y, vy[yi].y, vy[yj].y)
                    maxy = max(vx[xi].y, vx[xj].y, vy[yi].y, vy[yj].y)
                    
                    # 직사각형의 울타리 길이
                    k = (maxx - minx) * 2 + (maxy - miny) * 2
                    
                    # 나무 제거 개수와 울타리 포함되는 나무의 길이 합산
                    t = 0
                    cnt = 0
                    ww = []
                    for node in trees:
                        if minx <= node.x <= maxx and miny <= node.y <= maxy:
                            ww.append(node.w)
                        else:
                            t += node.w
                            cnt += 1
                    
                    # 울타리 길이 만족할 때까지 내부 나무 추가
                    ww.sort(reverse=True)
                    while k > t and ww:
                        t += ww.pop(0)
                        cnt += 1
                    
                    # 최소 나무 제거 개수 업데이트
                    if k <= t:
                        res = min(res, cnt)
    
    # 결과 출력
    print(res)

if __name__ == "__main__":
    main()
