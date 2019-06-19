def solution(money):
    answer = [0 for i in range(9)]
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 1] #지폐에 관한 배열

    for i in range(9):
        #만약 현재 남은 돈보다 나누려는 지폐가 크면 다음 지폐로 넘어감(10500, 1002 이런경우도 있으므로)
        if money<arr[i]:
            continue
        #answer에 가능한 지폐만큼 추가해줌
        answer[i] += money//arr[i]
        #남은 돈을 계산해줌
        money %= arr[i]
    return answer
