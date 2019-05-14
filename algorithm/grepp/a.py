n = int(input())

#n개에서 r개를 선택하는 중복조합임
#n+r-1 C r
#시간관계쌍 컴비네이션은 직접구현하지 않고 from itertools import combinations를 이용하겠음

from itertools import combinations

def solution(n):
    answer = 0
    bin_n = str(bin(n))[2:]
    zero = 0
    one = 0
    for i in range(len(bin_n)):
        if bin_n[i]=="0":
            zero+=1
        else:
            one+=1
    #일단 더 작아야하므로 0의 개수가 보다 작을때와 같을때를 나눠서 시작함
    #1사이에 0을 배치하는 위치는 (1의 개수+1)임
    #즉 (1의 개수 +1)H(0의 개수)
    #((1의 개수+1)+(0의 개수)-1) C (0의 개수)
    one_list = [i for i in range(one+1)]#combinations를 사용하기위해 리스트화
    #0의 개수가 작을 경우
    print(bin_n)
    for _zero in range(zero):
        temp = list(combinations(one_list, _zero))
        print(temp, len(temp))
        answer += len(temp)-1
        print(answer)
    #같을 경우
    return answer
print(solution(n))