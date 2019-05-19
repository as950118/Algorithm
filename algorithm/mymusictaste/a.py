def soulution(S):
    #S= str(input())
    #숫자만 추출
    num = ""
    for i in S:
        if i.isdigit():
            num+=i
    len_num = len(num)

    ret = ""
    #나머지가 1이라면 뒤에 2블록은 2,2
    if len_num%3 == 1:
        for i in range(3,len_num-3, 3):
            ret += num[i-3:i]+"-"
        ret += num[len_num-4:len_num-2]+"-"+num[len_num-2:]
    #나머지가 2라면 뒤에 1블록만 2
    elif len_num%3 == 2:
        for i in range(3,len_num-1, 3):
            ret += num[i-3:i]+"-"
        ret += num[len_num-2:]
    #나머지가 없다면 3개씩
    else:
        for i in range(3, len_num-1, 3):
            ret += num[i-3:i]+"-"
        ret += num[len_num-3:]
    return ret
print(soulution(str(input())))