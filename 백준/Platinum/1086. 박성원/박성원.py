'''
설명은
https://blog.naver.com/na_qa/223350405565
'''
from math import factorial  # 팩토리얼 계산
from math import gcd  # 최대공약수 계산

import sys  # sys 모듈 임포트

# 입력 함수 정의
input = lambda: sys.stdin.readline().strip()

# 숫자 개수 입력
n = int(input())

# 숫자 리스트 및 길이 리스트
numbers = [0] * n
number_lengths = [0] * n

# 숫자 입력 및 길이 계산
for i in range(n):
    num_str = input()
    numbers[i] = int(num_str)
    number_lengths[i] = len(num_str)

# k 입력
k = int(input())

# 모든 숫자 선택 비트 마스크
full_mask = 2**n - 1

# 각 숫자 선택 비트 마스크 리스트
bit_masks = [2**i for i in range(n)]

# 전체 길이 계산
total_length = sum(number_lengths)

# 나머지 저장 2차원 배열
remainders = [[0] * total_length for _ in range(n)]

# 나머지 계산
for i in range(n):
    max_length = total_length - number_lengths[i]
    for j in range(max_length + 1):
        remainders[i][j] = numbers[i] * 10**(max_length - j) % k

# 동적 프로그래밍 테이블
dp = [[-1] * (full_mask + 1) for _ in range(100)]


# 재귀 함수: 숫자 조합 선택 및 나머지 계산
def solve(length, bit_mask, remainder):
    # 모든 숫자 선택 완료
    if bit_mask == full_mask:
        return remainder == 0

    # 이미 계산된 경우
    if dp[remainder][bit_mask] != -1:
        return dp[remainder][bit_mask]

    dp[remainder][bit_mask] = 0

    for i in range(n):
        # 숫자가 선택되지 않은 경우
        if not bit_mask & bit_masks[i]:
            # 다음 숫자 선택 후 재귀 호출
            next_mask = bit_mask | bit_masks[i]
            next_remainder = (remainder + remainders[i][length]) % k
            dp[remainder][bit_mask] += solve(length + number_lengths[i], next_mask, next_remainder)

    return dp[remainder][bit_mask]


# 결과 계산
result = solve(0, 0, 0)

# 최대공약수 계산
gcd_value = gcd(result, factorial(n))

# 결과 출력
if result == 0:
    print("0/1")
else:
    print(f"{result // gcd_value}/{factorial(n) // gcd_value}")

