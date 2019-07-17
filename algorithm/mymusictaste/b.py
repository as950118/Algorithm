def solutions(message, K):
    arr_message = message.split(" ")
    arr_message_len = [len(i) for i in arr_message]
    len_arr = len(arr_message)

    ret = []
    sum_len = -1 #띄어쓰기 때문에
    for i in range(len_arr):
        #1은 띄어쓰기 개수
        temp = sum_len + arr_message_len[i] + 1
        #맞게 떨어지는 경우
        if temp == K:
            ret.append(arr_message[i])
            break
        #마지막에 띄어쓰기로 끝나는 경우
        elif temp+1 == K:
            ret.append(arr_message[i])
            break
        #초과하는 경우
        elif temp > K:
            break
        #그외는 계속 진행
        else:
            ret.append(arr_message[i])
        sum_len = temp
    return " ".join(ret)


print(solutions("The qucik brown fox jumps over the lazy dog", 39))