'''
설명
문자열의 길이(n)부터 1까지 슬라이딩 윈도우를 진행.
잘라진 문자열이 대칭인지 비교.
시간복잡도 O(n**2), 공간복잡도 O(n)
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n==1:
            return s[0]
        for i in range(n, 0, -1):
            for j in range(0, n-i+1):
                ceil = 0
                if i%2 == 1:
                    ceil = 1
                # 0, 3 s[0:1] s[2:3]
                if s[j:j+i//2] == s[j+i//2+ceil:j+i][::-1]:
                    return s[j:j+i]