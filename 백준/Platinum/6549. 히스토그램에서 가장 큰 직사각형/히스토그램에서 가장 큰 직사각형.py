import sys
input = sys.stdin.readline

def largest_rectangle_in_histogram(N, heights):
    stack = []
    max_area = 0
    heights.append(0)  # 모든 막대를 처리하기 위해 끝에 0을 추가 (센티널 값)

    for i in range(N + 1):
        current_height = heights[i]
        start = i

        # 현재 막대의 높이가 스택의 마지막 막대 높이보다 작거나 같으면 스택을 처리
        while stack and stack[-1][1] >= current_height:
            start, height = stack.pop()
            # 스택에서 꺼낸 높이를 기준으로 면적 계산
            max_area = max(max_area, (i - start) * height)
        
        # 현재 막대를 스택에 추가 (시작 인덱스와 높이)
        stack.append((start, current_height))
    
    print(max_area)  # 최대 직사각형의 넓이 출력

while True:
    read = list(map(int, input().split()))
    N = read[0]
    if N == 0:
        break  # N이 0이면 종료
    # 첫 번째 값을 제외한 나머지 리스트로 히스토그램 계산
    largest_rectangle_in_histogram(N, read[1:])
