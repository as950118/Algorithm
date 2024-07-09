def closest_pair_of_points(points):
    import sys
    import math

    def distance_squared(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def closest_pair_recursive(px, py):
        if len(px) <= 3:
            min_dist_sq = float('inf')
            for i in range(len(px)):
                for j in range(i + 1, len(px)):
                    min_dist_sq = min(min_dist_sq, distance_squared(px[i], px[j]))
            return min_dist_sq

        mid = len(px) // 2
        midpoint = px[mid]

        Qx = px[:mid]
        Rx = px[mid:]
        midpoint_x = midpoint[0]

        Qy = list(filter(lambda x: x[0] <= midpoint_x, py))
        Ry = list(filter(lambda x: x[0] > midpoint_x, py))

        min_dist_sq_left = closest_pair_recursive(Qx, Qy)
        min_dist_sq_right = closest_pair_recursive(Rx, Ry)
        min_dist_sq = min(min_dist_sq_left, min_dist_sq_right)

        strip = [p for p in py if abs(p[0] - midpoint_x) < math.sqrt(min_dist_sq)]
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j][1] - strip[i][1]) ** 2 >= min_dist_sq:
                    break
                min_dist_sq = min(min_dist_sq, distance_squared(strip[i], strip[j]))

        return min_dist_sq

    points.sort(key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    return closest_pair_recursive(points, py)

# 입력 처리
n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 가장 가까운 두 점의 거리의 제곱 계산
result = closest_pair_of_points(points)

# 결과 출력
print(result)
