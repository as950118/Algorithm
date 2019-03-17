def solution(number):
    answer = 0
    for i in range(1, number+1):
        i = str(i)
        for j in i:
            if j=='3' or j=='6' or j=='9':
                answer += 1
    return answer

print(solution(13))
print(solution(33))
