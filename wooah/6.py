def solution(totalTicket, logs):
    answer = []
    logarr = {}
    for log in logs:
        name, state, time = log.split()
        c,m,s = time.split(':') #분과 초만 사용할것이므로
        time = int(m)*60 + int(s)
        logarr[time] = [name,state]

    curtime = 0 #마지막으로 접속한 사람의 시간
    for t in logarr:
        name, state = logarr[t]
        #leave로그가 남았다는건 접속엔 성공했으나 나간것이므로 마지막이름을 제거해줌
        if state == 'leave':
            curtime = 0 #또한 현재 접속한 사람이 없으므로 curtime도 초기화해줌
            answer.pop()
            continue
        #접속가능
        if curtime+60<=t:
            #10시에 서버가 종료되므로
            if t+60>=3600:
                continue
            else:
                answer.append(name)
                curtime = t #마지막으로 접속한 시간을 바꿔줌

    return sorted(answer) #이름순으로 정렬
totalTicket = 2000
logs = [
    "woni request 09:12:29",
    "brown request 09:23:11",
    "brown leave 09:23:44",
    "jason request 09:33:51",
    "jun request 09:33:56",
    "cu request 09:34:02"
]
print(solution(totalTicket, logs))
