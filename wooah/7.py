def solution(cryptogram):
    answer = ''
    n = len(cryptogram)
    state = 0
    for i in range(n):
        #같은 문자 발견
        if (i!=n-1 and cryptogram[i] == cryptogram[i+1]) or (i!=0 and cryptogram[i] == cryptogram[i-1]):
            state = 1
            continue
        else:
            answer += cryptogram[i]
    #만약 같은문자가 있었다면 다시 반복해줌
    if state == 1:
        return solution(answer)
    #없다면 반환하고 종료
    return answer
print(solution("browoanoommnaon"))
