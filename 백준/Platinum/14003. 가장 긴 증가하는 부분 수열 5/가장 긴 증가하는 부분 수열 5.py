import sys
from bisect import bisect_left

# 입력을 빠르게 받기 위해 사용
input = sys.stdin.read

def find_lis(arr):
    n = len(arr)
    lis = []  # 증가 부분 수열을 저장할 리스트
    index_arr = [0] * n  # 각 원소의 LIS 위치를 기록할 배열

    # LIS 길이와 위치를 찾는 과정
    for i in range(n):
        if not lis or lis[-1] < arr[i]:  # LIS 리스트가 비어있거나, 현재 원소가 LIS의 마지막 원소보다 크다면
            lis.append(arr[i])
            index_arr[i] = len(lis) - 1  # 현재 원소의 LIS 위치 기록
        else:
            # 이분 탐색으로 현재 원소가 들어갈 위치 찾기
            pos = bisect_left(lis, arr[i])
            lis[pos] = arr[i]
            index_arr[i] = pos  # 현재 원소의 LIS 위치 기록

    # LIS 길이 출력
    print(len(lis))

    # LIS 구성 요소 찾기
    answer = []
    find_index = len(lis) - 1  # 마지막 인덱스부터 추적

    # 뒤에서부터 역추적하여 실제 LIS 원소들 찾기
    for i in range(n - 1, -1, -1):
        if index_arr[i] == find_index:
            answer.append(arr[i])
            find_index -= 1

    return answer

# 입력 처리
data = input().strip().split()
n = int(data[0])
arr = list(map(int, data[1:]))

# LIS 탐색
answer = find_lis(arr)

# LIS 순서대로 출력
print(" ".join(map(str, answer[::-1])))
