def solution(word):
    #암호문을 해독하기위한 dict
    arr = {'A':'Z', 'B':'Y', 'C':'X', 'D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N','N':'M','O':'L','P':'K','Q':'J','R':'I','S':'H','T':'G','U':'F','V':'E','W':'D','X':'C','Y':'B','Z':'A',' ':' '}

    answer = ""
    for alp in word:
        #대문자라면 암호로 대치하기만 하면됨
        if alp.isupper():
            answer += arr[alp]
        #소문자라면 대문자로 바꿔서 암호로 대치한후 소문자로 변경해줘야함
        else:
            answer += arr[alp.upper()].lower()
    return answer

print(solution('i Love You'))
