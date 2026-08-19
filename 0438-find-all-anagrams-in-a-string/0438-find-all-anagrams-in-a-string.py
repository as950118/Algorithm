'''
설명
s의 각 알파벳별 갯수를 계산해서 저장해둡니다.
p를 s만큼의 윈도우로 설정하며 1씩 슬라이딩하며 해당 문자열들의 알파벳별 갯수를 계산합니다.
매번 계산하기보다는 1씩 이동할때마다 첫번째 문자의 개수를 제거, 추가될 문자의 개수를 추가 하는 방식으로 처리합니다.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        count_s = {a: 0 for a in string.ascii_lowercase}
        count_p = {a: 0 for a in string.ascii_lowercase}
        ret = []
        for a in p:
            count_p[a] += 1
        for a in s[0:len_p]:
            count_s[a] += 1
        if count_s == count_p:
            ret.append(0) 
        for i in range(len_s-len_p):
            count_s[s[i]] -= 1
            count_s[s[i+len_p]] += 1
            if count_s == count_p:
                ret.append(i+1) 
        return ret

